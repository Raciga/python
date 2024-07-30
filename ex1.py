def arithematic():
    print("we have addition--press 1")
    print("subtraction--press 2")
    print("multiplication--press 3")
    print("division--press 4")
    print("module--press 5")

    print("welcome to our arithematic world!")
arithematic()

a=input()
if(a=="1"):
   print("enter the value")
   m=int (input())
   print("enter the sec value")
   n=int(input())
   def add(e,b):    
    print(e+b)
add(m,n)

if(a=="2"):
    def sub(num1,num2):
        print(num1-num2)
    sub(100,200)

if(a=="3"):    
    def mul(c,d):
        print(c*d)
    mul(2,10)
if(a=="4"):
    def div(s,j):
        print(s/j)
    div(2,5)
if(a=="5"):    
    def mod(num4,num3):
        print(num4%num3)
    mod(10,50)

    
    