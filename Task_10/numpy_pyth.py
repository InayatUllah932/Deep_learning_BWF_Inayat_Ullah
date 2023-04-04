# Inayat ullah 
# numpy practice in python 
print("-----------------")
import numpy as np
list = [1,2,3,4,6,3,0,10]
arr = np.array(list)
arr_1 = arr.reshape(2,4)

arr_2 = np.array([[6,2,3,9],[10,3,4,7]])
print("Arr_1\n",arr_1,"\n","arry_2\n",arr_2)

print("arr + arr_2 = ",arr_1+arr_2)
print("-----------------------")

# when you multiply by some number it will be multiply to the whole arry
print("Every numbers will be multiple of two ",2*arr_1)
print("-----------------------")

# In the same way we can perform multiplication division subtraction and so on
sub_arr = arr_1 - arr_2
print(sub_arr)
print("-----------------------")
 
# Mutiplication of arr
mult = arr_1 * arr_2
print(mult)
print("-----------------------")

# This was the simple operation between two arrys next we will check to performed operation on some perticular number in the arr
print(arr_1[0][0])
print(2*arr_1[0][0])
print("-----------------------")

sum_arr_p = arr_1[1][0] + arr_2[1][3]
print(sum_arr_p)
print("-----------------------")

print(arr_1 > arr_2)
print("-----------------------")


