row=4
while row>=1:
    collom=1
    while collom<=4:
        if row==1 or row==4 or collom==1 or collom==4:
            print("*",end="")
        else:
            print("#",end="")
        collom=collom+1
    print()
    row=row-1
    