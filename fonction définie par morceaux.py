import matplotlib.pyplot as plt
import numpy as np

#Question 1
def F(x):
    if x >= 0 and x < 1:
        return x
    elif x >= 1 and x < 2:
        return 1
    else:
        return None
       
#Question 2
current_value = 0
x = []
y = []
for i in range(199):
    x.append(current_value)
    y.append(f(current_value))
    current_value += 0.01

#Question 3
x = np.linspace(0,2,200)
y = []
for elt in x:
    y.append(f(elt))

plt.plot(x, y)
plt.grid()
plt.xlabel("x")
plt.ylabel("y")
plt.title("y=f(x)")
plt.axis([0, 2, 0, 1.5])
plt.show()
