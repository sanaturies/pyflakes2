
class Node:
    def __init__(self,dataval=None) :
        self.dataval=dataval
        self.nextval=None
class SlinkedList:
    def __init__(self) :
        self.headval=None
    def listprint(self):
        printval=self.headval
        while printval !=None:
            print(printval.dataval)
            printval=printval.nextval

list=SlinkedList()
list.headval=Node('mon')
e2=Node('tues')
e3=Node('wed')
e4=Node('thrus')
e5=Node('fri')
e6=Node('sat')
e7=Node('sun')
list.headval.nextval=e2
e2.nextval=e3
e3.nextval=e4
e4.nextval=e5
e5.nextval=e6
e6.nextval=e7
list.listprint()