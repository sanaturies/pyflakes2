
sentence='you are very very smart'
words='you are very handsome'
sensplit=sentence.split()
wordsplit=words.split()
for i in range(len(wordsplit)):
    result=sentence.find(wordsplit[i])
    if result != -1:
        print('sentence contains the the following string:', wordsplit[i],result)
    else:
         print('sentence does not contain the the following string:', wordsplit[i],result)
    

sentence='you are very very smart'
dictionary='you are very handsome'
sensplit=sentence.split()
wordsplit=dictionary.split()
for i in range(len(sensplit)):
    result=dictionary.find(sensplit[i])
    if result != -1:
        print('sentence contains the the following string:', sensplit[i],result)
    else:
         print('sentence does not contain the the following string:', sensplit[i],result)
    
#sniffer software

lst=['kill','war','violence','hi']

sentence="let's kill this love"
setence2='hi ilysm'
sentence3='war'
li=[sentence,setence2,sentence3]
for i in range(len(li)):
    for j in range(len(li)):
        result=li[i].find(lst[j])
        if result != -1:
            print('red flag for:', lst[j],':', li[i])
        else:
            pass


