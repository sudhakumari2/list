question=["How many continents are there?","What is the capital of India?","NG mei kaun se course padhaya jaata hai?"]
options=[["Four", "Nine", "Seven", "Eight"],["Chandigarh", "Bhopal", "Chennai", "Delhi"],["Software Engineering", "Counseling", "Tourism", "Agriculture"]]
solution=[3, 4, 1]
i=0
while i<len(question):
    print(i+1,question[i])
    j=0
    while j<=len(options):
        print(j+1,options[i][j])
        j=j+1
    a=int(input("enter the answer: "))
    if a==solution[i]:
        print("your answer is right")
    else:
        print("you are wrong")
        break
    i=i+1
