
#find prime 
nnum=5
def prime(n,i):
    
    if n==0 or n==1:
        return 'invalid number'
    elif n==i:
        return True
    elif n%i==0:
        return False
    i+=1
    return prime(n,i)
print(prime(nnum,2)) 
