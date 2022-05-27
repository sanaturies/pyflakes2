
#find number of islands when 1=land and 0=water
island=0
grid=[
    [1,1,0,0,0],
    [1,1,1,0,0],
    [1,0,0,0,0]
    ]
lst2='0,1'                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
lst3='1,0'
#adding zeros
for i in range(len(grid)):
    grid[i].append(0)
    grid[i].insert(0,0)
print(grid)

#identifying islands in the first list
for i in range(len(grid)):
    if lst2 in grid[0] or lst3 in grid[0]:
       print('island')

#identifying islands in the rest of the lists.
for i in range(-1,len(grid)-1):
    for j in range(len(grid[0])):
        if grid[i][j]==grid[i+1]:
            island+=1

print(island)