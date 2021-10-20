n=int(input('enter the nimber'))
i=1
sum=0
while i<n:
	if n%i==0:
		sum=sum+i
	i=i+1
if n==sum:
	print('parfect')
else:
	print('not parfect')