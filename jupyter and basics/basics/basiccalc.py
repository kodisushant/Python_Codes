opr = input("enter an operator (+ - * /): ")
a = int(input("enter ur 1st number "))
b = int(input("enter ur 2nd number "))

if opr == "+":
    print(f"output: {a+b}")
elif opr == "-":
    print(f"output: {a-b}")
elif opr == "*":
    print(f"output: {a*b}")
elif opr == "/":
    if b == 0:
        print("error")
    else:
        print(f"output: {a/b}")
else:
    print("wrong operator bro")