
integer=67
rem=0
l=[]
rem2=0
while integer > 0:
    rem=integer%2
    integer = integer//2
    print(rem)
    l.append(rem)
l.reverse()
print(l)
for i in range(len(l)):
    if l[i]==0:
        l[i]=1
    else: 
        l[i]=0
print(l)
rem=1
for j in range(len(l)):
    rem2=2*rem2+l[j]
print(rem2)

if ~integer==l:
    print(True)
else:
    print(False)







