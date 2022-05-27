
#bubble sort
array=[10,89,23,49,20,1]
for i in range(len(array)):
    for j in range(len(array)-1):
        if array[j]>array[j+1]:
            array[j],array[j+1]=array[j+1],array[j]
print(array)

#selection sort
array=[10,89,23,49,20,1]
for i in range(len(array)-1):
    select=i
    for j in range(i+1,len(array)):
        if array[select]>array[j]:
            select=j
    array[i],array[select]=array[select],array[i]
print(array)

#insertion sort
array=[10,89,23,49,20,1]
arrayplus=0
for i in range(len(array)+1):
    for j in range(i+1,len(array)):
        if array[j]<array[i-1]:
            arrayplus=array[j]
            array.pop(j)
            array.insert(i-1,arrayplus)
print(array)



        
        

    