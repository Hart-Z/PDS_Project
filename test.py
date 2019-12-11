import numpy as np
a = np.array([1,2,3,4])
b = np.array([2,3,4,5])

for x, y in zip(a,b):
    print(str(x),str(y))