# practice4

# n= 1+2+3+4+5.....n   = (n-1)!+n
n=5
def recursion(n):
    if n==1 or n==0:
        return 1
    return n+recursion(n-1)


print(recursion(5))
