# a=[16,19,11,15,10,12,14]
# i=0
# while i<len(a):
# 	j=0
# 	while j<len(a)-1:
# 		if a[j]>a[j+1]:
# 			a[j],a[j+1]=a[j+1],a[j]
# 		j+=1
# 	i+=1
# print(a)
from user input se swapping
a=int(input("enter the number of list:  "))
list=[ ]
i=0
while i<=a:
	num=int(input("enter num:  "))
	list.append(num)
	i=i+1
i=0
while i<len(list):
	j=0
	while j<(len(list)-i-1):
		if list[j]>list[j+1]:
			list[j],list[j+1]=list[j+1],list[j]
		j=j+1
	i=i+1
print(list)