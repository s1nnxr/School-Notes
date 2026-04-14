# Vykreslete polynom spolu s ulovými body
## řešení F(x) = x^3-4x^2+10
import matplotlib.pyplot as plt
import numpy as np
fi= [5,10,2,1]
def f(x):
    return x**3-4*x**2+10
def LagrangeovaMetoda(x, fi):
    n = len(fi)
    result = 0
    for i in range(n):
        term = fi[i]
        for j in range(n):
            if j != i:
                term *= (x - j) / (i - j)
        result += term
    return result
x_values = np.linspace(0, 5, 100)
f_values = [f(x) for x in x_values]
lagrange_values = [LagrangeovaMetoda(x, fi) for x in x_values]
plt.plot(x_values, f_values, label='F(x)')
plt.plot(x_values, lagrange_values, label='Lagrangeova metoda')
plt.scatter(range(len(fi)), fi, color='red', label='Ulové body')
plt.title('Lagrangeova metoda vs F(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()
plt.show()
