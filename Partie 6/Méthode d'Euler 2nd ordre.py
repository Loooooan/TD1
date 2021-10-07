import matplotlib.pyplot as plt

def euler(U0, H0, Te, tmax, Q, w0):
    U = [U0]
    H = [H0]
    T = [Te]
    t = 0
    i = 1
    while t < tmax:
        t += Te
        H.append(H[i-1] + Te*(-(w0/Q)*H[i-1] - (w0**2)*U[i-1]))
        U.append(U[i-1] + Te*H[i-1])
        T.append(t)
        i += 1
    return U, H, T

U0 = 2
H0 = 0
w0 = 6
Q = 8
tmax = 10
Te = 0.6*10**(-3)

solution = euler(U0, H0, Te, tmax, Q, w0)
u = solution[0]
u_point = solution[1]
t = solution[2]

plt.plot(t, u)
#Phase:
#plt.plot(h, u)
plt.show()
