number=[1,1,0,1]
sum=0
i=-1
a=0
while i>=(-len(number)):
    sum=sum+number[i]*2**a
    i-=1
    a+=1
print(sum)