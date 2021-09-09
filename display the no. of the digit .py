n=input("enter any number")
i=0
#str=str(n)
str1="  "
while i<len(n):
    if n[i]=="0":
        str1+="zero"
    elif n[i]=="1":
        str1+="One"
    elif n[i]=="2":
        str1+="two"
    elif n[i]=="3":
        str1+="three"
    elif n[i]=="4":
        str1+="Four"
    elif n[i]=="5":
        str1+="Five"
    elif n[i]=="6":
        str1+="six"
    elif n[i]=="7":    
        str1+="seven"
    elif n[i]=="8":
        str1+="Eight"
    elif n[i]=="9":
        str1+="Nine"
    i+=1
    str1+=" "
print(str1)