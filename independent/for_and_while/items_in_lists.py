
#Define a function called count that has two arguments called sequence and item. 
# Return the number of times the item occurs in the list.
# For example: count([1,2,1,1], 1) should return 3 (because 1 appears 3 times in the list).

def countitem(numlst,num):
    count=0
    for i in numlst:
        if i==num:
            count+=1
    return count

print(countitem([1,2,1,1],1))