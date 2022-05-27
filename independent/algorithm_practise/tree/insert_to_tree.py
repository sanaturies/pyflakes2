
#insert into a tree
class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
    def insert(self,data):
        if self.data:
            if data<self.data:
                if self.left==None:
                    self.left=Node(data)
                else:
                    self.left.insert(data)
            elif data>self.data:
                if self.right==None:
                    self.right=Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data=data  
    def printTree(self):
        if self.left!=None:
            self.left.printTree()
        print(self.data)
        if self.right!=None:
            self.right.printTree()  

root=Node(10)
root.insert(5)
root.insert(6)
root.insert(25)
root.insert(9)  
root.insert(60)   
root.printTree()