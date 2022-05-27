
#remove the element after the element given in a linked list

class Node:
    def __init__(self,dataval=None):
        self.dataval=dataval
        self.nextval=None

class lList:
    def __init__(self):
        self.headval=None
    def listprint(self):
        printval=self.headval
        while printval !=None:
            print(printval.dataval)
            printval=printval.nextval
    def removeafter(self,elem):
        headval=self.headval
        if headval!=None:
            if headval.dataval==elem:
                self.headval=headval.nextval
                headval=None
                return
        while headval!=None:
            if headval.dataval==elem:
                break
            prev=headval
            headval=headval.nextval.nextval
            if headval==None:
                return
            prev.nextval.nextval=headval.nextval
            headval=None


    
list=lList
list.headval=Node('a')
e2=Node('b')
e3=Node('c')
e4=Node('d')
e5=Node('e')
e6=Node('f')
e7=Node('g')
e8=Node('h')
list.headval.nextval=e2
e2.nextval=e3
e3.nextval=e4
e4.nextval=e5
e5.nextval=e6
e6.nextval=e7
e7.nextval=e8
list.removeafter(list,e7)
list.listprint(list)


    
