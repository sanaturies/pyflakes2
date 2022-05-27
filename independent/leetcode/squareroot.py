
#find squareroot of x without builtin operators and functions
x=89
for i in range(1,x//2):
    if i*i==x:
       print(i)
       break
    elif i*i>x:
        print(i-1)
        break