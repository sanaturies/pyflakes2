
#inserting and removeing elements in a linked list
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
    def atBeginning(self,newdata):
        NewNode=Node(newdata)
        NewNode.nextval=self.headval
        self.headval=NewNode
    def atEnd(self,newdata):
        NewNode=Node(newdata)
        if self.headval is None:
            self.headval=NewNode
            return
        last=self.headval
        while last.nextval:
            last=last.nextval
        last.nextval=NewNode
    def inBetween(self,middle_node,newdata):
        if middle_node is None:
            print(False)
            return
        NewNode=Node(newdata)
        NewNode.nextval=middle_node.nextval
        middle_node.nextval=NewNode
        
    def RemoveNode(self, Removekey):
        #if removekey is the headval
          HeadVal = self.headval
          if (HeadVal is not None):
            if (HeadVal.dataval == Removekey):
                self.headval = HeadVal.nextval
                HeadVal = None 
                return
        #finding the remove key
          while (HeadVal is not None):
                if HeadVal.dataval == Removekey:
                    break
                prev = HeadVal
                HeadVal = HeadVal.nextval
#when you don't find anything you just return nothing
          if (HeadVal == None):
           return
#removeing remove key
          prev.nextval = HeadVal.nextval
          HeadVal = None
list=SlinkedList()
node = Node('Mon')
list.headval=node
e2=Node('tues')
e3=Node('wed')
e4=Node('thrus')
e5=Node('fri')
e6=Node('sat')

list.headval.nextval=e2
e2.nextval=e3
e3.nextval=e4
e4.nextval=e5
e5.nextval=e6
list.atBeginning('sun')
list.atEnd('ello')

list.inBetween(e4,'sup')
list.RemoveNode('sun')
list.listprint()