import numpy as np
arr = np.array([[1,2],[2,3],[6,8]])
arr_1 = np.array([1,2])
arr_sum = arr + arr_1
print(arr_sum)
print("-----------")

row_mean = arr.mean(1)
print(row_mean)
row_mean.reshape(3,1)
print("-------")

demeaned = arr - row_mean.reshape(3,1)
print(demeaned)

print(demeaned.mean(1))