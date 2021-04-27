a= ["dog","racecar","car"]
a= ["flower","flow","flight"]
i=0
while i<len(a):
    j=0
    while j<i:
        if a[i][0] == a[j][0] and a[i][1] ==a[j][1]:
            print(a[i][0]+a[i][1])
        else:
            print("'''")
        j+=1
    i+=1