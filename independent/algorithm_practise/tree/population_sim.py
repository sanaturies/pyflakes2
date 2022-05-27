
class Sim:
    def __init__(self,data) -> None:
        self.left=None
        self.right=None
        self.data={
            'greenbug':0,
            'weebug':1,
            'stingwing':2,
            'furbill':2.1,
            'scalebeaks':3,
            'catclaws':4
        }
    def insert (self,data):
        if self.data:
            if data<self.data:
                if self.left==None:
                    self.left=Sim(data)
                else:
                    self.left.insert(data)            
            else:
                if self.right==None:
                    self.right=Sim(data)
                else:
                    self.right.insert(data)
        else:
            self.data=data
    def printTreePre(self):
        print(self.data)
        if self.left!=None:
            self.left.printTreePre()
        if self.right!=None:
            self.right.printTreePre()

bug=Sim(10)
bug.printTreePre()