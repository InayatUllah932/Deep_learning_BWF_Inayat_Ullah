# Inayat Ullah

import numpy as np
arr_1 = np.array([[1,2],[5,6]])
arr__2 = np.array([[3,4,1],[7,0,8]])
# dot product of arrys
dot_prod = np.dot(arr_1,arr__2)
print("dot product = ",dot_prod)
print("---------------------")

# Transpose of matrix
trans = arr__2.T
print("Transpos = ",trans)
print("---------------------")

# Invers of matric uding numpy 
invers = np.linalg.inv(arr_1)
print("Inverse of arr_1 = ",invers)
print("---------------------")

# squar root of arr_1 
sq = np.sqrt(arr__2)
print("Squar root = ",sq)
print("---------------------")

# Determinat using numpy 
detrmin = np.linalg.det(arr_1)
print("Determinat = ",detrmin)
print("---------------------")
