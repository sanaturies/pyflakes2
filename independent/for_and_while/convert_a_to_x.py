
#convert all 'a' charecters to 'x'
string=''
string2=''
phrase='A bird in the hand...'
for i in range(len(phrase)):
    if phrase[i]=='a' or phrase[i]=='A':
      string+='xx'
    else:
        string+=phrase[i]
print(string)

#convert all 'xx' to 'a'

for i in range(len(string)):
    if string[i]=='x':
        string2+='a'
    else:
        string2+=string[i]
print(string2)
