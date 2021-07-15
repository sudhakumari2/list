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

list_of_char=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
i=0
position=5
while i<position:
    list_of_char.append(list_of_char[0])
    list_of_char.remove(list_of_char[0])
    i+=1
print(list_of_char)

