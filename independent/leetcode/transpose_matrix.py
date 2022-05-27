
#get a grid and flip it clockwise
grid=[
    [6,8,9,1],
    [7,9,1,4]
]
grid2=[]
lst=[]
count=0
for i in range(len(grid[0])):
    for j in range(len(grid)):
        lst.append(grid[j][i])
    grid2.append(lst)
    lst=[]
print(grid2)