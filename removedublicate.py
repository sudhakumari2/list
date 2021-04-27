a=[2,4,6,4,3,8,6,3,4,3,9,7,4,3]
i=0
b=[]
c=0
while i<len(a):
	if a[i] not in b:
		b.append(a[i])
	i+=1
b.sort()
print(b)
# Remove duplicate in list