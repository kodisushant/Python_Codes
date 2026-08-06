x=int(input("Enter a number: "))
orig=x
sum=0
while x!=0:
    rem=x%10
    sum+=rem**3
    x=int(x/10)
if(orig==sum):
    print("Armstrong")
else:
    print("Not Armstrong")