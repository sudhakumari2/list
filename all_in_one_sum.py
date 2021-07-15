a = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
even_sum=0
even_count=0
odd_sum=0
odd_count=0
all_sum=0
all_count=0
i=0
while i <len (a):
    all_count+=1
    all_sum=all_sum+a[i]
    if a[i]%2==0:
        even_count+=1
        even_sum=even_sum+a[i]
    else:
        odd_count+=1
        odd_sum=odd_sum+a[i]
    i+=1
print("all_count", all_count,"all_sum=",all_sum,"all avrage=",all_sum/all_count,"even_count=",even_count," even_sum=", even_sum,"evevn avrage =",even_sum/even_count,"all_count", odd_count,"odd_sum=",odd_sum,"odd avrage=",odd_sum/odd_count)
