
# The letter value of a letter is its position in the alphabet starting from 0
# You are given three strings firstWord, secondWord, and targetWord, each consisting of lowercase English letters 'a' through 'j' inclusive.
# Return true if the summation of the numerical values of firstWord and secondWord equals the numerical value of targetWord, or false otherwise.

dct={}
firstword='acb'
secondword='cba'
targetword='cdb'
firststr=''
secondstr=''
targetstr=''
alpha=['a','b','c','d','e','f','g','h','j']
for i in range(len(alpha)):
    dct[alpha[i]]=str(i)
for i in firstword:
    firststr += dct[i]
for i in secondword:
    secondstr += dct[i]  
for i in targetword:
    targetstr += dct[i]   
firstint=int(firststr)
secondint=int(secondstr)
targetint=int(targetstr)
istargetint=firstint+secondint
if istargetint==targetint:
    print(True)
else:
    print(False)

