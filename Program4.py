# Write a program to generate a 3*5*8 3D array whose each element is 0.

import numpy as np

mat = np.zeros(3*5*8).reshape(3,5,8).astype(int)
print(mat)