
# given a list of pos and neg ints, rearrage the elements so that the positive and negitive numbers alternate. Order of the pos elems 
# should be preserved, same with the negitive ones.
# 0 is pos. 
# start with pos
# any extras appear at end of output.

lst=[-1,-2,3,4,-5,6]
pos=[]
neg=[]
new=[]
for i in lst:
    if i<0:
        neg.append(i)
    else:
        pos.append(i)

for i in range((len(pos)+len(neg))//2):
    print(i)
    if len(pos)>0:
        new.append(pos[0])
        pos.pop(0)
    if len(neg)>0:
        new.append(neg[0])
        neg.pop(0)
    print(new)

if len(pos)>=1:
    new.append(pos)
elif len(neg)>=1:
    new.append(neg)
print(new) 

#without extra memory
lst=[-1,-2,3,4,-5,6]
for i in range(len(lst)):
    for j in range(i):
        if lst[j]<0:
            x=lst[j]
            lst.pop(j)
            lst.append(x)
        else:
            x=lst[j]
            lst.pop(j)
            lst.append(x)

print(lst)
