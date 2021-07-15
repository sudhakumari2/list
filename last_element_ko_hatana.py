# Original lists:
# numbers=[2, 3, 9, 8, 2, 0, 39, 84, 2, 2, 34, 2, 34, 5]
# numbers.pop()
# print(numbers)

# numbers=[2, 3, 9, 8, 2, 0, 39, 84, 2, 2, 34, 2]
# n=len(numbers)
# (numbers.pop(n-1))
# numbers.pop(n-2)
# numbers.pop(n-3)
# print(numbers)

a=[12,13,17,10,20,18,11]
i=0
b=[]
while i<len(a):
    j=i+1
    l=[]
    while j<len(a):
        if a[i]+a[j]==30:
            l.append(a[i])
            l.append(a[j])
            b.append(l) 
        j+=1
    
    i+=1
print(b)


