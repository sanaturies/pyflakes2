
#recusive modulus finder
def mod(x):
    if x==0:
        return True
    if x==1:
        return False
    print(x)
    return mod(x-2)
print(mod(100))