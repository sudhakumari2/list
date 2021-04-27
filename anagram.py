a='army'
b='mary'
i=0
while i<(len(a)):
	j=0
	while j<len(b):
		j+=1
		i+=1
if a[i-1] in b:
	print('yes anagram h')
else:
	print('no')
