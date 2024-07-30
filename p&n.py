while(True):
    print("enter the number")
    a=int(input())
    if(a>0):
        print("this number is positive")
    elif(a<0):
        print("this is number negative") 
    else:
        print("this number is zero")
    print("if u need the continue again y & n")
    again=input()
    if(again!="y"):
        break
