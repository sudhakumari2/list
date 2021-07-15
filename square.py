num=int(input("enter a number"))
tem=num
while tem>0:
    rem=tem%10
    result=rem**rem
    s=result
    tem=tem//10
print(s)

    