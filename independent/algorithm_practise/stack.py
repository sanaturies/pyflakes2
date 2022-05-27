
#stack list
mystack=[]
for i in range(3):
    mystack.append('a')
    print(mystack)
for i in range(3):
    mystack.pop()
    print(mystack)

#deque stack
from collections import deque
mystack=deque()
for i in range(3):
    mystack.append('b')
    print(mystack)
for i in range(3):
    mystack.pop()
    print(mystack)