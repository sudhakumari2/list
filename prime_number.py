n=[]
i=1
while i<=200:
    j=1
    c=0
    while j<=i:
        if i%j==0:
            c=c+1
        j=j+1
    if c==2:
        n.append(j)
    i=i+1
print(n) 