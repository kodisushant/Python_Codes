x=int(input("Enter a number: "))
orig=x
num=0
while x!=0:
    rem=x%10
    num=num*10+rem
    x=int(x/10)
if(num==orig):
    print("Palindrome")
else:
    print("Not a palindrome")