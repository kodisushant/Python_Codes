a = float(input("enter 1st number "))
b = float(input("enter 2nd number "))
c = float(input("enter 3rd number "))

if a>b :
    if a>c:
        print(f"{a} is greatest of the three")
    else:
        print(f"{c} is greatest of the three")
else:
    if b>c:
        print(f"{b} is greatest of the three")
    else:
        print(f"{c} is greatest of the three")