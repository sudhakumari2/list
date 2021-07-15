n=int(input("enter any number"))
c=0
while n>0:
    if n%2==0:
        print("even no.",n)
        c+=1
    if c==4:
        break
    n=n-1
n=int(input("enter a number"))
c=0
i=1
while i<=3:
    if n%2==1:
        print("odd",n)
        c+=1
    if c==4:
        break
    n+=1
    

    
