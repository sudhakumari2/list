element=[1,2,1]
rev=[]
index=-1
while index>=-len(element):
    rev.append(element[index])
    index-=1
if rev==element:
    print("palindrome hai")
else:
    print("no")