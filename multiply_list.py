a=[2,3,4,5]
b=[3,4,1,2]
i=0
while i<len(a):
    j=0
    while j<len(b):
        if i==j:
            product=a[i]*b[j]
            print(product)
        j+=1
    i+=1


