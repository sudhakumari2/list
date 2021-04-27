a=[[1,5,3],[4,5,3],[9,5,3],[11,8,2,5 ,3]]
i=0
c=[]
while i<len(a):
	j=0
	b=0
	while j<len(a[i]):
		if a[i][j]== a[i][j]:
			b+=1
		if b>1:
			c.append(a[i][j])
		j+=1
		if len(c)==2:
			break
	i+=1
print(c)
# Print common elements in nested list