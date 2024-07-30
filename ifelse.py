print("enter the age")
age=int (input())
print("enter the gender")
gender=input()
if(age>=18 and age<30 and gender=="m"):
    print("wages=700")
elif(age>=18 and age<30 and gender=="f"):
    print("wages=750")
elif(age>=30 and age<=40 and gender=="m"):
    print("wages=800")
elif(age>=30 and age<=40 and gender=="f"):
    print("wages=850")
else:
    print("nil")               
    


