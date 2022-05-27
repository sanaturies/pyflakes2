
integer=list((input('num?')))
def numsum(integer):  
    integ=0
    for i in range(len(integer)):
        integer[i]=int(integer[i])
    for i in range(len(integer)):
        integ+=integer[i]
    return integ
def product(integer):
    integ=1
    for i in range(len(integer)):
        integer[i]=int(integer[i])
    for i in range(len(integer)):
        integ*=integer[i]
    return integ
print(product(integer)-numsum(integer))
