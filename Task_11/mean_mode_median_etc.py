# Inayat Ullah
import statistics as st
import numpy as np
from scipy.stats import rankdata

arr = np.array([1,2,3,4,5,3,5,6])
mean = np.mean(arr)
print("Mean = ",mean)
print("----------")

# median 

median = np.median(arr)
print("Median = ",median)
print("----------")

# mode 

mod = st.mode(arr)
print("Mode = ",mod)
print("----------")
Qunt = np.quantile(arr,0.25)
print(Qunt)
print("----------")

print(f"Average ranking:\n {rankdata(arr,method='average')}")
print("----------")

print(f"max ranking:\n {rankdata(arr,method='max')}")
print("----------")

print(f"min ranking:\n {rankdata(arr,method='min')}")