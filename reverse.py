numbers=[]
i=1
while i<=10:
    num=int(input("enter any number"))
    numbers.append(num)
    i+=1
print(numbers)
i=-1
n=[]
while i>=-(len(numbers)):
    n.append(numbers[i])
    i-=1
print(n)
sep:   string inserted between values, default a space.
end:   string appended after the last value, default a newline.
flush: whether to forcibly flush the stream.

