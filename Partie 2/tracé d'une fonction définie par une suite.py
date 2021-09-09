import matplotlib.pyplot as plt
import numpy as np

def F(c):
    #Valeurs & variables
    m=10
    M=20
    k_possible = []
    #Avoir les 10 premières valeurs de la suite u_k pour c fixé
    uk=[]
    u0=0
    u1=u0**2+c
    for i in range(10):
        if i == 0:
            uk.append(u0)
        else:
            u0=u1
            uk.append(u1)
            u1=u0**2+c
    #On regarde les valeurs entre 0 et m
    for i in range(m):
        #On vérifie que |u_k| > M
        if (uk[i]) > M:
            k_possible.append(i)
    #Si k existe, on retourne k
    if len(k_possible) > 0:
        return(min(k_possible))
    #Sinon, on retourne m+1
    else:
        return(m+1)
    #F(1) retourne 4

x = np.linspace(-2,2,400)
y = []
for elt in x:
    y.append(F(elt))

plt.plot(x, y)
plt.grid()
plt.xlabel("x")
plt.ylabel("y")
plt.title("y=F(x)")
plt.show()
