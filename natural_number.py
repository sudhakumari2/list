# i=1
# while i<=10:
#     if i%2==0:
#         print("even number hai",i)
#     else:
#         print("odd number hai",i)
#     i+=1

# i=1
# while i<=10:
#     print(i)
#     i+=1

# i=1
# while i<=10:
#     print(i*i)
#     i+=1

# num=int(input("enter a number"))
# product=1
# i=0
# while num>i:
#     rem=num%10
#     product=product*rem
#     num=num//10
# print(product)

# num=int(input("enter any number"))
# i=0
# while num>i:
#     rev=num%10
#     print(rev,end="")
#     num=num//10
    
# import math
# find Factorial of any number
# number=int(input("enter any number"))
# a=number
# while a>0:
#     Reminder = a % 10
#     i=1
#     Factorial=1
#     while i<=Reminder:
#         Factorial = Factorial*i
#         i+=1
#     a=a//10
# print(Factorial)
# b_num=input("enter any binary number ")
# sum=0
# i=-1
# a=0
# while i>(-len(b_num)):
#     sum=sum+int(b_num[i])*2**a
#     i-=1
#     a+=1
# print(sum)

# denominator = 1
# n=int(input("enter any number"))
# sum = 0
# while denominator <= n:
#     num = 1/denominator
#     sum += num
#     denominator += 1
# print(sum)

# n=int(input("enter any number"))
# rev=0
# num=n
# while n>0:
#     rev=(rev*10)+n%10
#     n//=10
# print(rev)
# if num==rev:
#     print("palindrome hai")
# else:
#     print("palindrome nhi hai")

# S = "Welcome to my Blog"
# print(S[2])
# print(S[2 : 10])
# print(S[-2 : ]) 

# print(S[-10 : -2 : 2])

# str1 = "Anita"
# if str1[1] == 'm':
#     print(str1)

# s1 = "   "
# s2 = "   Amit"
# print(s1.isspace())
# print(s2.isspace())

# str1 = "Welcome to my Blog"
# print(len(str1))
# print(capitalize(str1))

# str1 = "Welcome to my Blog my Blog "
# x = str1.split()
# b="Blog"
# c=[]
# i=0
# while i<len(x):
#     if x[i]==b:
#         c.append(x[i])
#     i+=1
# print(c)

# str1 = "Welcome to my Blog"
# print(str1.find('o'))
# print(str1.find('o',3))
# print(str1.find('o',7))
# print(str1.find('o',7,10))

# list1 = [1,2,3,4,5,6]
# list2 = [2,3,1,0,6,7]
# i=0
# list3=[]
# while i<len(list1):
#     if list1[i]not in list2:
#         list3.append(list1[i])
#     i+=1
# print(list3)

# second_name=input("enter second name")
# first_name=input("enter firsr name")
# print(first_name+"",second_name)

# num=int(input("enter a number"))
# i=1
# while i<num+1:
#     if num%i==0:
#         print(i)
#     i+=1

# i=1
# while i<=5:
#     j=5
#     while j>=i:
#         print(j,end=" ")
#         j-=1
#     print()
#     i+=1
# 5 4 3 2 1
# 5 4 3 2
# 5 4 3
# 5 4
# 5

# i=5
# while i>=1:
#     j=1
#     while j>=i:
#         print(i,end=" ")
#         j+=1
#     print()
#     i-=1

# str = "Python Output based Questions"
# word=str.split()
# for i in word:
#     print(i)

# for i in range(7,-2,-9):
#     # print(i)
#     for j in range(i):
#         print(j)

# for i in range(5):
#     # for j in i:
#     print("AS"*i,"\n")


# x = "Welcome to my blog"
# j = "i"
# while j in x:
#      print(j)

# s1="csworld.com"
# s2=""
# s3=""
# for x in s1:
#      if(x=="s" or x=="n" or x=="p"):
#            s2+=x
# print(s2,end=" ")
# print(s3)

# for i in range(5):
#     print(i)



