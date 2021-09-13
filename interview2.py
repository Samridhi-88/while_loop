list=['abc','xyz','aba','121']
i=1
c=0
while i<len(list):
    if list[i][0]==list[i][-1]:
        c=c+1
    i=i+1
print(c)