def dicho(f, a, b, epsilon):
    while b-a > epsilon:
        m = (b+a)/2
        if f(a)*f(m)<0:
            b = m
        else:
            a = m
    return(m)
