a=[5, 6, [], 3, [], [], 9]
i=0
new_list=[]
while i<len(a):
    if a[i]!=[]:
        new_list.append(a[i])
    i+=1
print(new_list)