n=[2,8,4,6,7]
max=0
i=0
sec_max=0
while i<len(n):
    if n[i]>max:
        max=n[i]
    i+=1
    index=0
    while index<len(n):
        if sec_max<n[index]<max:
            sec_max=n[index]
        index+=1
print(sec_max)
0
# n=[2,8,4,6,7]
# max=0
# i=0
# sec_max=0
# while i<len(n):
#     if n[i]>max:
#         max=n[i]
#     i+=1
#     index=0
#     while index<len(n):
#         if sec_max<n[index]<max:
#             sec_max=n[index]
#         index+=1
# print(sec_max)