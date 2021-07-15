# a=5
# def add_numberd():
#     b=6
#     return a
#     return b
# print(add_numberd())

# list1=[1,3,4,5]
# list2=list1.copy()
# print(list2)

# for i in range(10):
#     print(i)

pat = [1, 3, 2, 1, 2, 3, 1, 0, 1, 3]
for p in pat:
    pass
    if (p == 0):
        current = p
        break
    elif (p % 2 == 0):
        continue
    print(p)   
print(current)    

# def appendNumber(arr):
#     arr.append(4)

# arr = [1, 2, 3]

# print(arr)  
# appendNumber(arr)
# print(arr)  

# list=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
# i=1
# while i<len(list):
#     j=0
#     while j<len(list)-3:
#         list[j+3],list[j]=list[j],list[j+3]
#         j+=1
#     i+=1
# print(list)
    
# ['d', 'e', 'f', 'g', 'h', 'a', 'b', 'c']
# Iterate the said list cyclically on specific index position 5 :
# ['f', 'g', 'h', 'a', 'b', 'c', 'd', 'e']

# list=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
# res = []
# K=3
# i=0
# while i<len(list):
#     res.append(list[K % len(list)])
#     K = K + 1
#     i+=1
# print(res)

# list=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
# res = []
# i=3
# while i<len(list):
#     res.append(list[i])
#     i+=1
# i=0
# while i<len(list):
#     if i==3:
#         break
#     res.append(list[i])
#     i+=1
# print(res)

