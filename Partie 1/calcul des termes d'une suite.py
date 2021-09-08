def F1(n):
    u0 = 1
    u1 = 3*u0+5
    if n == 0:
        return 1
    for i in range(n-1):
        u0 = u1
        u1 = 3 * u0 + 5
    return u1

def F2(n):
    L = []
    for i in range(n+1):
        L.append(F1(i))
    return(L)
