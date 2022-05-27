
#group all things that are the same together
lst=['r','r','g','b','b','g','r']
lstset=set(lst)
lstlist=list(lstset)
for i in range(len(lstlist)):
    for k in range(len(lst)):
     if lst[k]==lstlist[i]:
        j=lst[k]
        lst.pop(k)
        lst.insert(0,j)
print(lst)


