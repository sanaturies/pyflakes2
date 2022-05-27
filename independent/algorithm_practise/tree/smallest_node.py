
#find the smallest and biggest nodes 
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
        if self.left != None:
            self.left.printTree()
        print(self.data )
        if self.right != None:
            self.right.printTree()

    def printsmallest(self):
        if self.left==None:
            print("smallest = ", self.data)
        else:
            self.left.printsmallest()
    def printBiggest(self):
        if self.right==None:
            print('biggest=', self.data)
        else:
            self.right.printBiggest()
        
root=Node(70)
root.insert(10)
root.insert(20)
root.insert(30)
root.insert(40)
root.printTree()
root.printsmallest()
root.printBiggest()
