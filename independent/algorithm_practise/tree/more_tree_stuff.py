
#what am i doing??????
#first we do baby steps
#find one num in the tree

class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data 
    def insert(self,data):
        if self.data:
            if data<self.data:
                if self.left is None:
                    self.left=Node(data)
                else:
                    self.left.insert(data)
            elif data>self.data:
                if self.right is None:
                    self.right=Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data=data
    def printTree(self):
        if self.left!=None:
            self.left.printTree()
        print(self.data)
        if self.right !=None:
            self.right.printTree()
    def findTree(self,num,found):
        if self.left != None:
            self.left.findTree(num,found)
        if self.data==num:
            print(True)
            found = True
        
        if self.right != None:
           self.right.findTree(num,found)

root=Node(40)
root.insert(10)
root.insert(20)
root.insert(70)
root.printTree()
found = False
root.findTree(10,found)
print(found)
                