num=int(input("enter any number"))
sum=0
while num>0:
    rem=num%10
    sum=sum+rem
    num=num//10
print(sum)