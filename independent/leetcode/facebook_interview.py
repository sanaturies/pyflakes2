
array=str(input('list?'))
arraysplit=array.split(',')
for i in range(len(array)):
    if array[i]=='0':
        arraysplit.insert(0,array[i])
        arraysplit.pop(i+1)
print(arraysplit)