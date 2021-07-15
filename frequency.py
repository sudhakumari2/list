list=[4, 6, 4, 3, 3, 4, 3, 4, 3, 8]
K = 3
res = [] 
i=0
while i<len(list):
    freq = list.count(i)  
    if freq > K and i not in res: 
        res.append(i)
    i+=1
    print(freq)
print(res)