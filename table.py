num1=int(input("enter first number"))
num2=int(input("enter second number"))
while num1<=num2:
    i=1
    while i<=10:
        print(num1,'*',i,'=',num1*i)
        i+=1
    print()
    num1+=1