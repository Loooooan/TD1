def rectdroite(f, a, b, n):
    res = 0
    h = (b-a)/n
    for i in range(n):
        res += h*f(a+i*h)
    return res
