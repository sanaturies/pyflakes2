
lst=['a','b','c','a','b','c']
window=set()
left=0
result=0
for r in range(len(lst)):
    while lst[r] in window:
        window.remove(lst[left])
        left+=1
    window.add(lst[r])
    result=max(result,r-left+1)
print(result)

