
DaysA = set(["Mon","Tue","Wed",])
DaysB = set(["Mon","Tue","Wed","Thu","Fri","Sat","Sun"])
setc={3,2,1}
setd={2,4}
SubsetRes = DaysA == DaysB #false?
SupersetRes = DaysA & DaysB
#SupersetRes=setd&setc
SupersetRes = DaysB|DaysA
setc.discard(2)
setc.add(9)
for i in setc:
    print(i)
print(SubsetRes)
print(SupersetRes)
print(setc)

#removes common elements