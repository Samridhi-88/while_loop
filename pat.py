i=int(input("enter the num"))
while i>=1:
    j=1
    while j<=i-1:
        print("",end="")
        j=j+1
    k=1
    while k<=i:
        print("*",end="")
        k=k+1
    print()
    i=i-1