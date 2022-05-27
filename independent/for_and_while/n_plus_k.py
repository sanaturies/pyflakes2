
# n is the num k is the number of times n is repeated.
n='2'
k=3
lst=[]
string=''
added=0
for i in range(k):
    string+=n
    lst.append(string)
print(lst)

for i in range(len(lst)):
    lst[i]=int(lst[i])
    added+=lst[i]
print(added)