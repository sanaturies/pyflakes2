
#find sum of all digits
num=234
lst=[]
num=str(num)
runningsum=0
for i in range(len(num)):
    lst.append(int(num[i]))
    runningsum+=lst[i]
print(runningsum)
