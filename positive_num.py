a=int(input("enter a number"))
b=int(input("enter a number"))
c=a%b
d=a-c
if d%b==0:
    print(d)
else:
    print("nothing")