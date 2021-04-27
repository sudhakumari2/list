a=[[1,4,5],[1,3,5],[2,6]]
i=0
b=[]
while i<len(a):
	j=0
	while j<len(a[i]):
		b.append(a[i][j])
		j+=1
	i+=1
b.sort()
