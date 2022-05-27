
#tell the user how many numbers are smaller than list[i] in the given list
lst=[6,7,8,1,4,5,89]
lstsort=sorted(lst)
lst2=[]
for i in range(len(lst)):
    y=lstsort.index(lst[i])
    lst2.append(y)

print(lst2)