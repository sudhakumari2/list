# a=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# i=-1
# b=[]
# while i>(-len(a)):
#     c=a[i]-a[i-1]
#     b.append(c)
#     i-=1
# print(b)

a=[2, 4, 6, 8]
i=-1
b=[]
while i>(-len(a)):
    c=a[i]-a[i-1]
    b.append(c)
    i-=1
print(b)