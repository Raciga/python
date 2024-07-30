start=int(input())
end=int(input())
count=0
even=0
for n in range(start,end):
   if(n%2==1):
     print("odd numbers",n)
     count=count+1
   elif(n%2==0):
      print("even numbers",n)
      even=even+1
print("the final number is",count) 
print("the final number is",even)    
    

