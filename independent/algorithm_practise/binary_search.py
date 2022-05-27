
array=str(input('list of nums?'))
arraysplit=array.split()
for i in range(len(arraysplit)):
    arraysplit[i]=int(arraysplit[i])
arraysplit.sort()
target=int(input('target'))
mn=arraysplit[0]
mx=arraysplit[-2]
i=0
guess=0
if target in arraysplit:    
    while i != target:
        if arraysplit[i]==target:
            print(i,guess,target)
            break
        elif target<arraysplit[i]:
            mn=arraysplit[i]+1
            i+=1
            guess+=1
        else:
            mx=arraysplit[i]-1
            i+=1
            guess+=1
else:
    print('sorry, the target number is not in the list')