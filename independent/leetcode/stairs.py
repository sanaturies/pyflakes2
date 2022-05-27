
import math
n=4
if n>=3:
    x=2
    y=n//2
    x+=y
    x+=math.factorial(y)
    print(x)
else:
    print(n)