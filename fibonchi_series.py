
# def fib(n):
#     p, q = 0, 1
#     while(p < n):
#         yield p
#         p, q = q, p + q

# x = fib(10)
# print(x)
original_list=[ ['g', 'f', 'g'], ['i', 's'], ['b', 'e', 's', 't'] ]
i=0
while i<len(original_list):
    j=0
    while j<len(original_list[i]):
        print(original_list[i][j],end="")
        j+=1
    i+=1


                                   