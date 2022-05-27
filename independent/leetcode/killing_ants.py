
left=[None,None,None,None,None,None,None,None]
right=[0,1,2,3,4,5,6,7]
time=0
for i in range(1,(len(left))):
    if left[i]==None and right[i]!=None:
        right[i]+=1
        right.insert(i-1,None)
        right.pop(0)
        time+=1
    elif right[i]==None and left[i]!=None:
        left[i]+=1
        left.insert(i-1,None)
        left.pop(0)
        time+=1
    elif right[i]==None and left[i]==None:
        right.pop(i)
        left.pop(i)
        time+=1
    elif left[i]!=None and right[i]!= None:
        right1=right[i]
        right[i]=left[i]
        left[i]=right1
    else:
        print(time)
print(time)