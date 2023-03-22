# Inayat Ullah
print("---------")
# To check the type of set
Set = {"Inayat","Bilal","kashi","Omair"}
print(type(Set))
print("---------")

#duplicate value in the set is not acceptable
Set = {1,2,3,4,2}
# 2 in the set is duplicate which will print once in the ternmenl
print("2 is Duplicate which will print once in the set ",Set)
print("---------")

# Sting int and boolean in the set
Set = {"Inayat",52,"anayat2019@namal.edu.pk",True}
print(Set)
print("---------")

#Acces elements in the set
print("elements in the set one by one ")
for i in Set:
    print(i)
print("---------")

# We can not get elements by indexing in the set
# Union Intersection and other operation on the set
set_1 = {1,2,3,8}
set_2 = {2,5,7,3}
print("First_Set = ",set_1,"\n","Second_set = ",set_2)
print("Union over first and second set = ",set_1.union(set_2) )
print("---------")

# Intersection 
print("Intersection between set_1 and set_2 = ",set_1.intersection(set_2))
print("---------")

# Difference in set!
First = {7,2,0,4,5,3,1,6}
print("First set = ",First)
second = {2,10,9,6}
print("Second set = ",second)
print("First - second = ",First.difference(second))
print("---------")

#Symmatric Difference in set
print("Symmatric = ",First.symmetric_difference(second))
print("---------")

