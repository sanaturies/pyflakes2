
num=0
new_num=0
count=1
p=num
while p>0:
    m=num%10
    new_num = new_num*10 + p%10 
    p//=10
print(new_num)
if new_num==num:
    print(True)
else:
    print(False)