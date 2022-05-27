
def running_sum():
    array=str(input('list of nums?'))
    array2=array.split(',')
    for i in range(len(array2)):
        array2[i]=int(array2[i])
    new_array=[]
    j=0
    append_num=0
    for i in range(0,len(array2)):
        append_num+=array2[j]
        new_array.append(append_num)
        j+=1
    print('output:',new_array) 
running_sum()       