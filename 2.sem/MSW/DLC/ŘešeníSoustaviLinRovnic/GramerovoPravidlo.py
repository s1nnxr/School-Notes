# Implementace gramerova pravidla v pythonu
# Soustavu rovnic o *n* s nenulovým determinantem soustavy d_A \not = 0 má
# právě jedno řešení x_1,...,x_n kde
# x_i=\frac{d_{ai}}{d_a}
# kde d_{ai} je determinant soustavi, který vznikne z d_a tak, že nahradíme i-tý sloupec vektorem pravých stran
# Spočítejte pomocí cramerova pravidla řešení x_1, x_2, x_3 následující soustavy
# 3x1+2x2+x3=5
# 2x1+3x2+x3=1
# 2x1+x2+3x3=11

import numpy as np

A = np.array([
    [3, 2, 1],
    [2, 3, 1],
    [2, 1, 3]
])
b = np.array([5, 1, 11])
dA = np.linalg.det(A)
if dA==0:
    exit(1)
n = A.shape[0]
x = []
for i in range(n):
    Ai = A.copy()
    Ai[:, i] = b
    dAi = np.linalg.det(Ai)
    x.append(dAi / dA)
for i in range(n):
    print(f"x{i+1} = {x[i]}")
