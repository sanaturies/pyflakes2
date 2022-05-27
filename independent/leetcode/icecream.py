
#most icecreams you can buy
costs=[1,6,3,1,2,5]
coins=20
icecreams=0
total=0
costs.sort()
for i in range(len(costs)):
    total+=costs[i]
    icecreams+=1
    if total>coins:
        print(icecreams-1)
        break
    elif i==len(costs)-1:
        print(icecreams)
        break
