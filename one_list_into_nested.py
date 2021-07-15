array = [4, 5, 5, 5, 3, 8]
i=0
while i<len(array)-2:
    i+=1
    if array[i] == array[i + 1] and array[i + 1] == array[i + 2]:
        print(array[i])
