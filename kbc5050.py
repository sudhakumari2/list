question=["How many continents are there?","What is the capital of India?","NG mei kaun se course padhaya jaata hai?"]
options=[["Four", "Nine", "Seven", "Eight"],["Chandigarh", "Bhopal", "Chennai", "Delhi"],["Software Engineering", "Counseling", "Tourism", "Agriculture"]]
solution=[3, 4, 1]
l_s=[['four','seven'],['delhi','bhopal'],['tourism','software engineerinh']]
solution_2=[2,1,2]
i=0
c=0
while i<len(question):
    print(question[i])
    j=0
    while j<len(options[i]):
        print(options[i][j])
        j=j+1
    a=int(input("enter the option: "))
    if a==solution[i]:
        print("your answer is right")
    elif a==5050:
    	if c==0:
    		print('this is your 5050 option')
    		k=0
    		while k<len(l_s[i]):
    			print(l_s[i][k])
    			k+=1
    			c+=1
    		s=int(input('enter the option'))
    		if s==solution_2[i]:
    			print('congrats your answer is correct')
    		else:
    			print('you are out of the game')
    			break
    	else:
    		print('you already used 5050')
    		n=int(input("select yr option:"))
    		if n==solution[i]:
    			print("congrats ur answer is correct")
    		else:
    			print("wrong answer")
    			break
    else:
       print("sorry ur choosed wrong answer")
       print("quit")
       break
    i=i+1