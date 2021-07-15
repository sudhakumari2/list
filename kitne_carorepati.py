a = [3000, 600000, 324990909, 90990900, 30000, 5600000, 690909090, 31010101, 532010, 510, 4100]
i=0
count=0                                                                         
crorepati=0
lakhpati=0
dilwale=0
while i< len(a):
    n=i
    while n>0:
        temp=n%10
        count+=1
        n=n//10
        if count>=8:
            crorepati+=1
        elif count==6 or count==7:
            lakhpati+=1
        elif count<=5:
            dilwale+=1
    i+=1
print("crorepati= ",crorepati, "lakhpati=",lakhpati, 'dilwale= ', dilwale)