x=int(input("enter a number: "))
orig=x
sum=0
while x!=0:
	rem=x%10
	fact =1
	while rem!=0:
		fact*=rem
		rem-=1
	sum+=fact
	x/=10
if(sum==orig):
	print("strong number")
else:
	print("not strong number")