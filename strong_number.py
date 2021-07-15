import math
for number in range(1,200):
    a=number
    sum=0
    while a>0:
        Reminder = a % 10
        Factorial = math.factorial(Reminder)
        sum=sum+Factorial
        a=a//10
    if sum==number:
        print("strong number hai",number)
    else:
        print("strong number nhi h",number)
w

# i=100
# while i<=150:
#     a=i
#     sum=0
#     while a>0:
#         fac=1
#         k=1
#         rem=a%10
#         while k<=rem:
#             fac=fac*k
#             k+=1
#         sum=sum+fac
#         a=a//10
#     i+=1
#     if sum==i:
#         print("strong number hai",i)
#     else:
#         print("strong number nhi hai",)

