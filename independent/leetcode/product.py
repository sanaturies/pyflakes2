
#return whether the product of a list is poitive, negative, or zero
nums=str(input('list of nums?')) 
num=nums.split(',')
output='positive'
inital='positive'
marker='positive'
for i in range(len(num)):
    num[i]=int(num[i])
for i in range(len(num)):
    if num[i]>0:
        marker='positive'
    elif num[i]<0:
        marker='negitive'
    else:
        pass
    if 0 in num:
        flag='nuteral'
    elif marker=='positive' and inital=='positive':
        flag='positive'
    elif marker=='negitive' and inital=='positive':
        flag='negitive'
    elif intial=='negitive' and marker=='positive':
        flag='negitive'
    elif marker=='negitive' and inital=='negitive':
        flag='negitive'
print('the product of all nums in the list is', flag)