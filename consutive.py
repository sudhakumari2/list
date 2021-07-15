# a=[1, 1, 64, 23, 64, 22, 22, 22]
# i=0
# c=0
# while i<len(a):
#     c+=1 
#     i+=1
# if c==3:
#     print(a[i])

i=0
a=[]
while i<5:
    num=int(input("enter a number"))
    a.append(num)
    sorted_l=sorted(a)
    i+=1
range_list=list(range(min(a),max(a)+1))
if range_list==sorted_l:
    print("true,consutive h")
else:
    print("no")

