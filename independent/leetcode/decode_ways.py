
'''
A message containing letters from A-Z can be encoded into numbers using the following mapping:

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:

"AAJF" with the grouping (1 1 10 6)
"KJF" with the grouping (11 10 6)
Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

Given a string s containing only digits, return the number of ways to decode it.

The answer is guaranteed to fit in a 32-bit integer.

'''
newstring=[]
encode={}
alpha='abcdefghijklmnopqrstuvwxyz'
for i in range(len(alpha)):
    encode[alpha[i]]=str(i+1)
print(encode)
split=[]
s='11106'
'''
last_split=0
lindex=0
#for m in range(1,len(s)+1):
sindex = 0
eindex = 2
for n in range(len(s)):
    substr = s[sindex:eindex]
    sindex += 1
    eindex += 1
    #print (substr)
    #print(" ")'''
last_split=0
accepted=[]
for  i in range(1,len(s)+1):
    for j in range(0,len(s)+1,i):
        if i==1:
            split_by=s[last_split:j]
            split_by=list(split_by)
            split.append(split_by)
            last_split=j
        #else:
            #break

print(split)


last_split=0
for  i in range(1,len(s)+1):
    for j in range(0,len(s)+1,i):
        if i==1:
            split_by=s[last_split-1:j]
            split_by=list(split_by)
            split.append(split_by)
            last_split=j
print(split)
for i in split:
    for j in i:
        if j in encode:
            letter=encode.get(i)
            print(letter)
            newstring.append(letter)
            print(newstring)
