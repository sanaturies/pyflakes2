
#write a program that prints out all the elements of the list that are less than "less_than".

def less_than(lst,less_than):
    for i in lst:
        if i<=less_than:
            print(i)
    return

less_than([1,2,3,8,9,10,60,21,13,17,34],20)

#above in a list
def less_than_improved(lst,less_than):
    lst2=[]
    for i in lst:
        if i<=less_than:
            lst2.append(i)
    return lst2

print(less_than_improved([1,2,3,8,9,10,60,21,13,17,34],10))

#the same thing in only one line
lst3=[1,2,3,8,9,10,60,21,13,17,34]
less_than=20


