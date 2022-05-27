
userlist=list(input('word/sentence? '))
userlist.sort()
jls_extract_var = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for i in jls_extract_var:
    if i in userlist:  
       flag=True
    else:
        flag=False
if flag==True:
    print('sentence is a panagram')
else :
    print('sentence is not a panagram')