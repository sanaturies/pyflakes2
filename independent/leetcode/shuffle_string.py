
#take a str with a list of given indeces, reorder the str to the given indeces.
word=list(input('word?'))
indeces=list(input('indeces?'))
newlist=[]
for i in range(len(indeces)):
    indeces[i]=int(indeces[i])
for i in range(len(word)):
    newlist.insert(indeces[i], word[i])
print(newlist)