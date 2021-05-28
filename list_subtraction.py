number=[[7,2,3,4,5,6],[1,2,3,4,5,6]]
i=0
a=[]
while i<=0:
    j=0
    while j<len(number[i]):
        b=number[0][j]-number[1][j]
        a.append(b)
        j=j+1
    i=i+1
print(a)


