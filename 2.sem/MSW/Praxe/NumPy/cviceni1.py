import time
import numpy as np

velikostVektoru = 1000000

def SoucetSeznamy1():                   # klasické for
    t1 = time.time()
    X = range(velikostVektoru)
    Y = range(velikostVektoru)
    Z = []
    for i in range(len(X)):
        Z.append(X[i] + Y[i])
    return time.time() - t1

def SoucetSeznamy():
    t1 = time.time()
    X = range(velikostVektoru)
    Y = range(velikostVektoru)
    Z = [X[i] + Y[i] for i in range(len(X)) ]
    return time.time() - t1

def SoucetNumPy():                      # numpy
    t1 = time.time()
    X = np.arange(velikostVektoru)
    Y = np.arange(velikostVektoru)
    Z = X + Y
    return time.time() - t1

print(SoucetSeznamy1())
t1 = SoucetSeznamy()
t2 = SoucetNumPy()
print(t1)
print(t2)
if t2 != 0:
    print("Numpy je rychlejší {:.2f}×".format(t1/t2))
else:
    print("Podíl nelze stanovit")
