#mutiplucation by two
num=10
y=1
x=[]
i=0
while i < num+1:
    x.append(y)
    y+=y
    i+=1
print(x)

#actualy fibonacci
num=10
y=1
x=[0]
i=0
while i < num+1:
    x.append(y)
    y+=x[i-1]
    i+=1
print(x)

#actualy fibonacci 2
num=9
y=1
p1=1
p2=1
i=0
print(y)
while i < num+1:
   y=p1+p2
   p1=p2
   p2 =y
   i+=1
   print(y)

#factorial
n = 5
fact = 1
  
for i in range(1,n+1):
    fact = fact * i     
print ("The factorial of %s is : " %(n))
print (fact)

#factorial
import math
num=int(input("number!"))
factorial=math.factorial(num)
print(factorial)