
#place n queens in an n*n board such that they can't attack eachother
#logic, place them all a knight's lenght away from each other

n=4
board=[]
for i in range(n*n):
    board.append(board)
print(board)
#for i in range(n):
board[2][1].append('Q')
        
print(board)


