
#iteritive factorial
num=4
factorial=1
for i in range(1,num+1):
    factorial*=i
print(factorial)

#iteritive fibbonacci
num=9
num+=1
y=1
x=[]
i=0
while i < num+1:
    x.append(y)
    y+=x[i-1]
    i+=1
print(x)

#version 2 iteritive fibbonacci
num=9
y=1
p1=1
p2=1
i=0
while i < num+1:
   y=p1+p2
   p1=p2
   p2 =y
   i+=1
print(y)
    