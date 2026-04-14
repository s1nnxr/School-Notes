# Numpy je rychlejší protože je compilován
import numpy as np

for typ in np.ScalarType:print("Typ v NumPY:",typ)
# Vytvoření maticí a vectorů
vector = np.array([1,2,3,4])
matice = np.array([[1,2],[3,4],[5,6]])

# Manipulace matice
print(matice.shape)
print(matice.size)
print(sys.getsiteof(matice))
matice.dtype

# Generace jednorozměrného pole
print(np.array(range(20))) # od 0 až 19
print(np.arange(4,20))     # od 4 až 19
print(np.arange(4,20,2))   # od 4 až 19 po 2
