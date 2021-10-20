num=int(input("enter any number="))
sum=0
n=num
while num:
	rem=num%10
	sum=sum+rem
	num=num//10
if (n%sum==0):
    print("is a harshad number")
else:
    print(" not a harshad number")