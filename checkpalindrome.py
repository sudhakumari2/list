a='babab'
i=0
c=[]
while i<len(a):
		c.append(a[i])
		i+=1
index=-1
rev=[]
while index>=(-len(c)):
	rev.append(c[index])
	index-=1
if rev==c:
	print('palindrome h',rev)
else:
	print('no')