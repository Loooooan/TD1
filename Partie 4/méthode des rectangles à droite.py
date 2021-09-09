import scipy.integrate as sc

def f(x):
    return x**2

def rectdroite(f, a, b, n):
    res = 0
    h = (b-a)/n
    for i in range(n):
        res += h*f(a+i*h)
    return res

print(rectdroite(f, 0, 1, 500))
#Affiche rectdroite(f, 0, 1, 500)
print(sc.quad(f, 0, 1))
#Affiche (0.33333333333333337, 3.700743415417189e-15)
