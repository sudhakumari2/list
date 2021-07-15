a=[12, 67, 98, 34]
res=[]
i=0
while i<len(a):
    sum=0
    while a[i]>0:
        c=a[i]%10
        sum=sum+c
        a[i]=a[i]//10
    i+=1
    res.append(sum)
print(res)