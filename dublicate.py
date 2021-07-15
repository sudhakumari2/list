List = [6,1,3,5,6,3,1]
i=0
c=[]
while i<len(List):
    if List[i] not in c:
        c.append(List[i])
    i+=1
i=0
product=1
while i<len(c):
    product=(c[i]*product)
    i+=1
print(product)

# list=[1,2,2,5,8,4,4,8]
# i=0
# a=[]
# c=0
# while i<len(list):
#     if list[i] not in a:
#         c+=1
#         a.append(list[i])
#     i+=1

# print(a)

