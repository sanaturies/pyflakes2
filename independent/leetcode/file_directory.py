
#file changing directory
path=["d1/","d2/","../","d21/","./"]
stack=[]
starting=path[0]
location=path[0]
for i in range(1,len(path)):
    stack.append(location)
    if path[i]!=location:
        if path[i]=='./':
           pass
        elif path[i]=='../':
            location=starting
        else:
            location=path[i]
    else:
        pass

