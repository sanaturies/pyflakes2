
#find all missing nums
lst=[0,1,3,4,6,9,8]
lst.sort()
for i in range(len(lst)-1):
    if lst[i]+1==lst[i+1]:
        print(None)
    else:
        print(lst[i]+1)