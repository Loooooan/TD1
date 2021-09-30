def Euler(y0, t0, Te, N, E, tau):
    Y = [y0]
    T = [t0]
    time = Te
    for i in range(1,N):
        Y.append(Y[i-1] + Te*(E-Y[i-1])/tau)
        T.append(time)
        time += Te
    return T, Y

import matplotlib.pyplot as plt

tau = 30*(10**-3)
E = 10
N = 1000
Te = 0.2*(10**-3)
t0 = 0
y0 = 0

L = Euler(y0, t0, Te, N, E, tau)
t = L[0]
y = L[1]

plt.plot(t,y)
plt.show()
