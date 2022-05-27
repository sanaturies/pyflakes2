
#compress an image
#coding by guru 
bitmap = [[0,0,1,1,1,1,0,0,1],[1,1,0,0,0,0,1,1,0],[1,0,1,0,1,0,1,0,1]]
encodelist = []

for line in range(len(bitmap)):
    whites = 0
    blacks = 0
    wCounting = True
    encoderow = []
    for i in range(len(bitmap[line])):
        if(bitmap[line][i] == 0 and wCounting):
            whites += 1
        if(bitmap[line][i] == 1 and not wCounting):
            blacks += 1
        #transitions      
        if (bitmap[line][i] == 1 and wCounting):
            encoderow.append(whites)
            whites = 0
            blacks += 1
            wCounting = False
        elif (bitmap[line][i] == 0 and not wCounting):
            encoderow.append(blacks)
            blacks = 0
            whites += 1
            wCounting = True
    #left over edge cases
    if (whites > 0):
        encoderow.append(whites)
    if (blacks > 0):
        encoderow.append(blacks)
    encodelist.append(encoderow)
       
#output
for j in range(len(encodelist)):
    print (encodelist[j])


#reversing the encoded list
unencode=[]
for i in range(len(encodelist)):
    for j in range(len(encodelist[i])):
        if j%2==0:
            unencode.append('0'*encodelist[i][j])
        else:
            unencode.append('1'*encodelist[i][j])

for i in range(len(encodelist)):
    n=len(encodelist[i])
    if encodelist[i-1]==']':
        unencode.insert(i,'[')
    if i == n:
        unencode.insert(i,']')
print(unencode)