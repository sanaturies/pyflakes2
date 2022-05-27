
#Create a for loop that prompts the user for a hobby 3 times, then appends each one to hobbies

def hobbies():
    lst=[]
    for i in range(3):
        append=input('hobby? ')
        lst.append(append)
    return lst
print(hobbies())