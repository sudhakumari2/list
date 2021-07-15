a=[34.67, 12, -94.89, 'Python', 0, 'C#']
i=0
result=[]
while i<len(a):
    if type(a[i])==int:
        result.append(a[i])
    i+=1
print(result)
