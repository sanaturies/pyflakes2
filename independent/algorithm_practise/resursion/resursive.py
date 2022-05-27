
#recuh
#rsive factorial
num=4
def fact(n):
    if n==0 or n==1:
        return 1
    return n*fact(n-1)
print(fact(num))

#recursive fibbonacci
f=10
def Fib(n):
     if n==1 or n==0:
        return 1
     else:
        return Fib(n-1)+Fib(n-2)
print(Fib(f-1))

#recursive palindrome
palindrome=list(input('str?'))
def pal(p):
    for i in range(len(p)):
        if len(p)==0 or len(p)==1:
            return 'it is a palimdrome'
        else:
            if p[0]==p[-1]:
                p.pop(0)
                p.pop(-1)
                return pal(p)
            else:
                return 'it is not a palindrome'
print(pal(palindrome))

#recursive powers
#x^n
n_num=3
x_num=8
def powers(x,n):
    if n==0:
        return 1
    else:
        return x*powers(x,n-1)
print(powers(x_num,n_num))

#optimized recursive powers
#x^n
nnum=(-1)
xnum=8
def power(x,n):
    if n==0:
        return 1
    elif n>0 and n%2==0:
       # recursively compute y=x^(n/2)
       y=x*power(x, n/2)
       return y*y
    elif n>0 and n%2==1:
        #recursively compute x^(n-1)
        #x^n=x^(n-1) * x
        y=x*power(x, n-1)
        return y
    elif n<0:
        #recursively compute n^(-n)
        #x^n = 1/x^(-n)
        y=power(x, abs(n))
        return 1/y
print(power(xnum,nnum))



