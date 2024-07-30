import random


#a=random.randint(1,1000)
count=0
wrong=0
print("welcome to the program")
while(True):
    first=random.randint(1,100)
    print("the first number is:",first)
    second=random.randint(100,200)
    print("the second number is:",second)
    print("enter your answer")
    result=int(input())
    third=first+second 
    if(third==result):
        print("true")
        count=count+1
    else:
        print("flase") 
        wrong=wrong+1
    print("do you want continue y or n")   
    con=input()
    if(con!="y"):
        break
print("the correct answer is",count)  
print("the wrong answer is",wrong)  