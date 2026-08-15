import numpy as np

# Activation function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Network weights
print("="*60)
print("RESTAURANT RATING PREDICTOR - MATRIX REPRESENTATION")
print("="*60)

# Weights from Input to Hidden Layer (3x3 matrix)
W1 = np.array([
    [0.5, 0.3, 0.8],  # Hidden neuron 1
    [0.7, 0.4, 0.2],  # Hidden neuron 2
    [0.2, 0.9, 0.6]   # Hidden neuron 3
])

print("\nW1 (Input → Hidden) weights:")
print("Rows: Hidden neurons | Cols: [Price, Distance, Bias]")
print(W1)

# Weights from Hidden to Output Layer (1x4 matrix)
W2 = np.array([
    [0.6, 0.5, 0.8, 0.3]  # Output neuron
])

print("\nW2 (Hidden → Output) weights:")
print("Cols: [H1, H2, H3, Bias]")
print(W2)

# Input: [Price=7, Distance=3, Bias=1]
X = np.array([[7], [3], [1]])

print("\n" + "="*60)
print("FORWARD PROPAGATION")
print("="*60)

print("\nInput Vector X:")
print(f"Price: {X[0][0]}")
print(f"Distance: {X[1][0]}")
print(f"Bias: {X[2][0]}")

# Step 1: Input to Hidden Layer
print("\n--- STEP 1: Calculate Hidden Layer ---")
hidden_input = W1 @ X  # Matrix multiplication
print(f"\nHidden Layer Input (before activation):")
print(f"H1 input: {hidden_input[0][0]:.3f}")
print(f"H2 input: {hidden_input[1][0]:.3f}")
print(f"H3 input: {hidden_input[2][0]:.3f}")

# Manual calculation for H1 (shown as example)
h1_manual = (7 * 0.5) + (3 * 0.3) + (1 * 0.8)
print(f"\nH1 calculation breakdown:")
print(f"(7 × 0.5) + (3 × 0.3) + (1 × 0.8) = {h1_manual:.3f}")

# Apply activation
hidden_output = sigmoid(hidden_input)
print(f"\nHidden Layer Output (after sigmoid):")
print(f"H1 output: {hidden_output[0][0]:.3f}")
print(f"H2 output: {hidden_output[1][0]:.3f}")
print(f"H3 output: {hidden_output[2][0]:.3f}")

# Add bias to hidden output
hidden_with_bias = np.vstack([hidden_output, [[1]]])

# Step 2: Hidden to Output Layer
print("\n--- STEP 2: Calculate Output Layer ---")
output_input = W2 @ hidden_with_bias
print(f"\nOutput Input (before activation): {output_input[0][0]:.3f}")

# Manual calculation
output_manual = (hidden_output[0][0] * 0.6) + (hidden_output[1][0] * 0.5) + \
                (hidden_output[2][0] * 0.8) + (1 * 0.3)
print(f"\nOutput calculation breakdown:")
print(f"({hidden_output[0][0]:.3f} × 0.6) + ({hidden_output[1][0]:.3f} × 0.5) + " + 
      f"({hidden_output[2][0]:.3f} × 0.8) + (1 × 0.3)")
print(f"= {output_manual:.3f}")

# Apply final activation
final_output = sigmoid(output_input)

print("\n" + "="*60)
print("FINAL PREDICTION")
print("="*60)
print(f"\nRestaurant Rating: {final_output[0][0]:.3f}")
print(f"Rating Percentage: {final_output[0][0]*100:.1f}%")
print(f"\nInterpretation: {'EXCELLENT!' if final_output[0][0] > 0.8 else 'GOOD' if final_output[0][0] > 0.6 else 'AVERAGE'}")

# Test with different inputs
print("\n" + "="*60)
print("TESTING DIFFERENT RESTAURANTS")
print("="*60)

test_cases = [
    ([3, 2], "Cheap & Close"),
    ([9, 8], "Expensive & Far"),
    ([5, 5], "Moderate Price & Distance"),
]

for inputs, description in test_cases:
    X_test = np.array([[inputs[0]], [inputs[1]], [1]])
    h_input = sigmoid(W1 @ X_test)
    h_bias = np.vstack([h_input, [[1]]])
    output = sigmoid(W2 @ h_bias)[0][0]
    print(f"\n{description} (Price={inputs[0]}, Dist={inputs[1]}): {output:.3f} ({output*100:.1f}%)")