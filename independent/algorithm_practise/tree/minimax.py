
# pickup sticks in minimax algorithm

class Pickupsticks:
    def __init__(self,sticks):
       self.sticks=sticks
       self.positive=0
       self.negigtive=0
    def Countdown(self,list,sum):
        if sum==0 and self.sticks%2!=0:
            return 'you won'
       
        return Countdown(list.append(sum-1), sum-1,self.sticks+1) and Countdown(list.append(sum-2), sum-2,self.sticks+1)

s=Pickupsticks(7)
s.Countdown([], 7)