'''
Title:
Implement a Mini-Batch Gradient Descent Neural Network From Scratch

Objective:
Extend the basic neural network implementation to support Mini-Batch Gradient Descent instead of SGD. You will still solve the same XOR classification task, but the training loop must work differently.

Requirements:
	Neural Network Architecture
		- Same as Program-1: 2-hidden-layer architecture learning XOR
		- Activation function must be sigmoid

	Training Method – Mini-Batch GD
		- A mini-batch size (e.g., 2) should be used
		- Inside each batch:
			* Perform forward pass for each sample
			* Compute deltas via backprop for each sample
			* Accumulate gradients across the batch
		- After processing the batch:
			* Apply a single weight update using average gradients

	What You Must Implement
		- Gradient accumulator structure (same shape as weights)
		- Batch-wise update logic
		- Shuffle training examples each epoch
		- Maintain detailed correctness in backprop and forward passes
		- Prediction function

Expected Output
Print error every few epochs
After training, show the classification results for XOR inputs

Goal
Learn how mini-batch GD reduces noise in updates compared to SGD
and understand its importance in stabilizing neural network training.

Actual Output:
epoch=0 error=2.4755
epoch=1000 error=1.7219
epoch=2000 error=0.0788
epoch=3000 error=0.0289
epoch=4000 error=0.0173

Predictions after training (Mini-batch GD):
[0, 0, 0] -> 0
[0, 1, 1] -> 1
[1, 0, 1] -> 1
[1, 1, 0] -> 0

'''
# minibatch_backprop_xor.py
from math import exp
from random import random, seed, shuffle

# ----- Network helpers -----

def initialize_network(n_inputs, n_hidden, n_outputs):
    network = []
    hidden_layer = [{'weights': [random() for _ in range(n_inputs + 1)]}
                    for _ in range(n_hidden)]
    network.append(hidden_layer)
    output_layer = [{'weights': [random() for _ in range(n_hidden + 1)]}
                    for _ in range(n_outputs)]
    network.append(output_layer)
    return network

def activate(weights, inputs):
    activation = weights[-1]
    for i in range(len(weights) - 1):
        activation += weights[i] * inputs[i]
    return activation

def transfer(activation):
    return 1.0 / (1.0 + exp(-activation))

def forward_propagate(network, row):
    inputs = row
    for layer in network:
        new_inputs = []
        for neuron in layer:
            activation = activate(neuron['weights'], inputs)
            neuron['output'] = transfer(activation)
            new_inputs.append(neuron['output'])
        inputs = new_inputs
    return inputs

def transfer_derivative(output):
    return output * (1.0 - output)

def backward_propagate_error(network, expected):
    for i in reversed(range(len(network))):
        layer = network[i]
        errors = []
        if i != len(network) - 1:
            for j in range(len(layer)):
                error = 0.0
                for neuron in network[i + 1]:
                    error += neuron['weights'][j] * neuron['delta']
                errors.append(error)
        else:
            for j, neuron in enumerate(layer):
                errors.append(neuron['output'] - expected[j])
        for j, neuron in enumerate(layer):
            neuron['delta'] = errors[j] * transfer_derivative(neuron['output'])

# ----- Mini-batch gradient helpers -----

def zero_gradients(network):
    grads = []
    for layer in network:
        layer_grads = []
        for neuron in layer:
            layer_grads.append([0.0 for _ in neuron['weights']])
        grads.append(layer_grads)
    return grads


def accumulate_gradients(network, row, grads):
    for i in range(len(network)):
        inputs = row[:-1] if i == 0 else [neuron['output'] for neuron in network[i - 1]]
        layer = network[i]
        layer_grads = grads[i]
        for n_idx, neuron in enumerate(layer):
            for j in range(len(inputs)):
                layer_grads[n_idx][j] += neuron['delta'] * inputs[j]
            layer_grads[n_idx][-1] += neuron['delta']  # bias



def apply_gradients(network, grads, l_rate, batch_size):
    for i, layer in enumerate(network):
        for n_idx, neuron in enumerate(layer):
            for j in range(len(neuron['weights'])):
                grad_ij = grads[i][n_idx][j] / float(batch_size)
                neuron['weights'][j] -= l_rate * grad_ij

def train_network_minibatch(network, train, l_rate, n_epoch, n_outputs, batch_size):
    for epoch in range(n_epoch):
        sum_error = 0.0
        data = list(train)
        shuffle(data)

        for start in range(0, len(data), batch_size):
            batch = data[start:start + batch_size]
            current_batch_size = len(batch)
            grads = zero_gradients(network)

            for row in batch:
                inputs = row[:-1]
                outputs = forward_propagate(network, inputs)
                expected = [0 for _ in range(n_outputs)]
                expected[int(row[-1])] = 1
                sum_error += sum((expected[i] - outputs[i]) ** 2
                                 for i in range(n_outputs))
                backward_propagate_error(network, expected)
                accumulate_gradients(network, row, grads)

            apply_gradients(network, grads, l_rate, current_batch_size)

        if epoch % 1000 == 0:
            print(f"epoch={epoch} error={sum_error:.4f}")

def predict(network, row):
    outputs = forward_propagate(network, row)
    return outputs.index(max(outputs))

# ----- Demo on XOR -----

if __name__ == "__main__":
    seed(1)

    dataset = [
        [0, 0, 0],
        [0, 1, 1],
        [1, 0, 1],
        [1, 1, 0],
    ]

    n_inputs = 2
    n_hidden = 2
    n_outputs = 2

    network = initialize_network(n_inputs, n_hidden, n_outputs)
    train_network_minibatch(network, dataset,
                            l_rate=0.5,
                            n_epoch=5000,
                            n_outputs=n_outputs,
                            batch_size=2)

    print("\nPredictions after training (Mini-batch GD):")
    for row in dataset:
        print(row, "->", predict(network, row[:-1]))
