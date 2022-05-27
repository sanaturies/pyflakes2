
# second attempt
import random
board={
        1: "empty",
        2: "empty",
        3: "empty",
        4: "empty",
        5: "empty",
        6: "empty",
        7: "empty",
        8: "empty",
        9: "empty",
}
computer_X=[]
computer_x=random.randint(1,9)
computer_X.append(computer_x)
X=board.update({computer_x:"X"})
print(computer_X)
box="computer filled box %s" %(computer_X[0])
print(box)
def user():
        user_O=[]
        global user_o
        user_o=int(input("box number?"))
        user_O.append(user_o)
        O=board.update({user_o:"O"})
def computer(computer_X, computer_x,user_O):
        nextbox=random.randint(1,3)
        boolen=False
        print(computer_X)
        def check(computer_x,nextbox):
                if board[computer_x] == "empty":
                   board.update({computer_x:"X"}) 
                   boolen=True   
                else:
                   nextbox=random.randint(1,3)  
                   boolen=False
        while boolen==False:
                if nextbox==1:
                 if computer_X==9:
                        check(computer_x,nextbox)
                        computer_x-=1
                        print (computer_x)
                        print("computer filled box %s" %(computer_x))
                 else:
                        check(computer_x,nextbox)
                        computer_x+=1
                        print(computer_x)
                        print("computer filled box %s" %(computer_x))
                        print (computer_x)
                elif nextbox==2:
                 if computer_x>7:
                        check(computer_x,nextbox)
                        computer_x-=3
                        print (computer_x)
                        print("computer filled box %s" %(computer_x))
                 else:
                        check(computer_x,nextbox)
                        computer_x+=3
                        print(computer_X)
                        print("computer filled box %s" %(computer_x))
                        print (computer_x)
                elif nextbox==3:
                 if computer_x>5:
                        check(computer_x,nextbox)
                        computer_x-=4
                        print (computer_x)
                        print("computer filled box %s" %(computer_x))
                 else:
                        check(computer_x,nextbox)
                        computer_x+=4
                        print("computer filled box %s" %(computer_x))
                        print(computer_X)
        board.update({computer_x:"X"})
for i in range(8):
        user()
        computer(computer_X,computer_x,user_o)
        print(board)


 