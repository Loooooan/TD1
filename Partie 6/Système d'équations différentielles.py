import matplotlib.pyplot as plt

def euler(X0, Y0, Te, N):
    X = [X0]
    Y = [Y0]
    T = [0]
    for i in range (1, N+1):
        X.append(X[i-1] + Te * (X[i-1] * (2 - Y[i-1])))
        Y.append(Y[i-1] + Te * (Y[i-1] * (X[i-1] - 1)))
        T.append(i*Te)
    return (X, Y, T)

X0 = 3
Y0 = 1
Te = 1*10**(-3)
N = 7000

solution = euler(X0, Y0, Te, N)
x = solution[0]
y = solution[1]
t = solution[2]

plt.plot(t, x, linestyle='--')
plt.plot(t, y)
plt.legend(['x', 'y'])
plt.title("Méthode d'Euler")
plt.xlabel("t")

#Question d):
#plt.plot(y, x)
#plt.title("y en fonction de x")

plt.show()

