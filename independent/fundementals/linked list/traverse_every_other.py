


class Node:
    def __init__(self,dataval=None) :
        self.dataval=dataval
        self.nextval=None
class llist:
    def __init__(self):
        self.headval=None
    def listprint(self):
        printval=self.headval
        while printval!=None:
            print(printval.dataval) 
            if printval.nextval == None:
                return
            else:
                if printval.nextval.nextval != None:
                    printval = printval.nextval.nextval 
                else:
                    return      
        
    def makelist(self,lst):
        i=0
        llst=llist
        node=Node(lst[0])
        for i in range(len(lst)):
            if i==0:
                llist.headval=node
            else:
                temp=Node(lst[i])
                node.nextval=temp
                node=node.nextval
        node = None

        #else:
            #re.nextval=llst.makelist(self,lst)
            #return lst2.append(re.nextval)
lst=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
lst2=[]
llist.makelist(llist,lst)
'''a=Node('a')
b=Node('b')
c=Node('c')
llist.headval=a
a.nextval=b
b.nextval=c'''
llist.listprint(llist)
