def fac_iterative(n):
    fac=1
    for i in range (n):
        fac=fac*(i+1)
    return fac
print(fac_iterative(5))

def fac_recur(n):
    if n==1:
        return 1
    else:
        return n*fac_recur(n-1)
print(fac_recur(5))