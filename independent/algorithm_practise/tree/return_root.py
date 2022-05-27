
lst=[8,6,4,7,10,9,11]
order='preorder'
if order=='inorder':
    print(lst[len(lst)//2])
elif order=='preorder':
    print(lst[0])
else:
    print(lst[-1])