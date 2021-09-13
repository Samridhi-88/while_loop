#prime number
# n=int(input("enter any number"))
# count=0
# i=1
# while (i<=n):
# 	if (n%i)==0:
# 		count=count+1
# 	i=i+1
# if (count==2):
#     print("prime number")
# else:
#     print("composite number")


i=0
b=0
while i<=100:
	j=2
	count=0
	while j<=i//2:
		if i%j==0:
			count=count+1
			break
		j+=1
	if count==0 and i!=1:
		print(i,"prime")
	else:
		print(i,"not prime")
	i+=1