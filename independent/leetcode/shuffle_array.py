
list1=list(input('list of nums: '))
newlist=[]
lenlist1=len(list1)
half1=int(lenlist1/2)
firsthalf1=list1[:half1]
secondhalf1=list1[half1:lenlist1]
if lenlist1%2==0:
    for i in range(len(firsthalf1)):
        newlist.append(firsthalf1[i])
        newlist.append(secondhalf1[i])
else:
    u=lenlist1-1
    oddlist=list1[0:u]
    v=list1[lenlist1]
    for i in range(len(firsthalf1)):
        newlist.append(firsthalf1[i])
        newlist.append(secondhalf1[i])
    newlist.append(v)
print(newlist)
'''lenlist1=len(list1)
lenlist2=len(list2)
half1=int(lenlist1/2)
half2=int(lenlist2/2)
firsthalf1=list1[:half1]
secondhalf1=list2[half1:lenlist1]
firsthalf2=list1[:half2]
secondhalf2=list2[half2:lenlist1]'''


