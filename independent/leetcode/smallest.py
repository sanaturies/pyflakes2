
array=str(input('nums?'))
arraysplit=array.split()
counter=[]
for num in arraysplit:
    count=0
    for element in arraysplit:
        if (num > element):
            count+=1
    counter.append(count)
for num1 in counter:
    print(num1)
'''smaller=str(input('list of nums'))
smallersplit=smaller.split(',') 
mylist=[]
output=[]
counter=0
dic={}
for i in range(len(smallersplit)):
    smallersplit[i]=int(smallersplit[i])

smallersort=smallersplit.sort

for i in range(len(smallersplit)):
    v=smallersplit[i]
    count=smallersort.index(v)
    dic[v]=count

for i in smallersort:
    mylist.append(smallersort.index(i))

for i in smallersplit:
    j=smallersort[i]
    dic_j=dic[j]
    aight=mylist[i]
    print(aight)
    output.insert(aight,smallersort[i])'''



