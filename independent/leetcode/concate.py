
#accept two lists and see if they are the same when concated. 
word1=str(input('list of gibberish words: '))
word2=str(input('second list of gibberish words: '))
'''word1split=word1.split()
word2split=word2.split()
newword1=''
newword2=''
for i in range(len(word1split)):
    newword1+=word1split[i]
for i in range(len(word2split)):
    newword2+=word2split[i]'''
if word1 == word2:
    print(True)
else:
    print(False)


