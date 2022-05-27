
ugw=int(input('num?'))
count=0
while ugw > 0:
    if ugw%2==0:
        ugw/=2
        count+=1
    else:
        ugw-=1
        count+=1
print('%s steps'%count)