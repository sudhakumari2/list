# split_join.py

# nums = "1,5,6,8,2,3,1,9"

# n = nums.split(",")
# print(n)

# m = ':'.join(n)
# print(m)

# partition.py

# s = "1 + 2 + 3 = 6"

# a = s.partition("=")

# print(a)

# # We use the partition() method in this example.

# a = s.partition("=")

# convert_case.py

# a = "ZetCode"

# print(a.upper())
# print(a.lower())
# print(a.swapcase())
# print(a.title())

# list=[["a","b"],["c","d"]]
# c=[]
# i=0
# while i<len(list):
#     j=0
#     while j<len(list[i]):
#         c.append(list[i][j])
#         j+=1
#     i+=1
# i=0
# while i<len(c):
#     j=i+1
#     while j<len(c):
#         print(c[i]+c[j])
#         j+=1
#     i+=1
    

# a=input("enter any sentece")
# # b=input("enter any sentence")
# c=[]

# if b in a:
#     c.append(b)
# print(c)

# a="cup is on the table"
# b="on"
# if b in a:
#     print(a.replace(b, ""))
a=["amngo","banana","apple"]
a.pop()
print(a)