
#[int:big parking space, Int:medium parking space, int:small parking space]; a=big b=medium c=small
lst=[0,2,3]
cars=['a','b','b','c']
result=[]
parking=lst[0]*['a'] + lst[1]*['b'] + lst[2]*['c']
j = 0
for  i in range(len(cars)):
    if (cars[i] == parking[j] ):
         result.append('T')
         j += 1
    else:
        result.append('F')
print(result)  


#same thing different logic
park=[0,2,3]
cars=['a','b','b','c']
result=[]
cara=cars.count('a')
carb=cars.count('b')
carc= cars.count('c')
c=[cara,carb,carc]

for  i in range(len(c)):

    if c[i] > park[i]:
        if park[i] != 0 :
         result.append('true,'*park[i])
         result.append('false'*(c[i]-park[i]))
    elif c[i]<park[i]:
         result.append('true,'*c[i])   
    else:
         result.append('true,'*c[i])
print(result)

#same thing but samller cars can go into bigger spaces
lst=[0,2,3]
cars=['a','b','b','c']
result=[]

def can_fit(result,car):
    result.sort()
    j=0
    parking=lst[0]*['a'] + lst[1]*['b'] + lst[2]*['c']
    for i in range(len(car)):
         if cars[i] == parking[j]:
             result.append('T')
             j += 1
         elif cars[i]=='b' and parking[j]=='a':
             result.append('T')
         elif cars[i]=='c'and parking[j]=='b' or cars[i]=='c' and parking[j]=='a':
             result.append('T')
         else:
             result.append('F')
    return result

print(can_fit(result, cars))        

