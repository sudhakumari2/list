a=[2,3,4,5,11]
b=[1,9,8,7,9]
a.extend(b)
d=[]
i=0
while i<len(a):
    if a[i] not in d:
        d.append(a[i])
    i+=1
d.sort()
print(d)
