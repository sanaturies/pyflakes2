
#roman to integer
# I=1
# V=5
# X=10
# L=50
# C=100
# D=500
# M=1000
count=0
roman='LM'
numerals={
    'I' : 1,
    'V' : 5,
    'X':10,
    'L':50,
    'C':100,
    'D':500,
    'M':1000
    }
#print(numerals[roman[0]])
roman=roman[::-1]
prev=roman[0]
for i in range(len(roman)):
    if roman[i] in numerals:
        if numerals[roman[i]]>=numerals[prev]:
            count+=numerals[roman[i]]
            prev=roman[i]
        else:
            count-=numerals[roman[i]]
            prev=roman[i]
print(count)