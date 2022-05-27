
#[frequncy,value,frquency,value]
decompress=[7,9,2,1]
i=0
j=0
output=[]

while i < len(decompress):
     frequency=decompress[i]
     i+=1
     value=decompress[i]
     i+=1
     j=0
     while j < frequency:
         output.append(value)
         j+=1
print (output)
'''
#opposite 1
compress=[3,3,3,3,3,1,8,8,9,9,9]
output=[]
count=0
val=compress[0]
while i < len(compress):
    if compress[i]!= val:
        output.append(count)
        output.append(val)
        count=0
        val=compress[i]
    else:
        i+=1
        count+=1
print(output)'''

#opposite 2
compress=[3,3,3,3,3,1,8,8,9,9,9]
compresscopy=compress.copy()
compresscopy=set(compress.copy())
output=[]
count=0
val=compress[0]
compresscopylist=list(compresscopy)
print("compress copy list", compresscopylist)
for i in  compresscopylist:
    frequency=compress.count(i)
    output.append(frequency)
    output.append(i)
print(output)


