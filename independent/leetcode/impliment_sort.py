
#c,c,a,a,b,b
#two pass insertion
tosort=['c','b','b','a','a','c']
ccount=tosort.count('c')
print(ccount)
for i in range(len(tosort)):
    if tosort[i]=='c':
        y=tosort[i]
        tosort.pop(i)
        tosort.insert(0,y)
    elif tosort[i]=='a':
        y=tosort[i]
        tosort.pop(i)
        tosort.insert(ccount,y)
    elif tosort[i]=='b':
        y=tosort[i]
        tosort.pop(i)
        tosort.insert(-1,y)
for i in range (len(tosort)):
    if tosort[i]=='b':
        y=tosort[i]
        tosort.pop(i)
        tosort.insert(-1,y)
print(tosort)

#selection sort
tosort=['a','b','b','c','a','c']
ccount=tosort.count('c')
j=0
for i in range(len(tosort)):
    if tosort[i]=='c':
         y=tosort[i]
         tosort[i],tosort[j]=tosort[j],y
         j+=1
print(tosort)

m=j
for  j in range(j,len(tosort)-1):
        if tosort[j]!='a':
             y=tosort[m]
             tosort[i],tosort[j]=y,tosort[i]
             m+=1
print(tosort)   
    
