
#count the number of times a charecter apperes in a str
string='ugiuilh'
char='g'
def count(string1,char1):
    char_count=0
    for i in string1:
        if i==char1:
            char_count+=1
    return char_count
print(count(string,char))

#remove duplicates
string2='uiop'
def remove_duplicate(string):
    string1=''
    for i in string:
        if i not in string1:
            string1+=i
    return string1
print(remove_duplicate(string2))   