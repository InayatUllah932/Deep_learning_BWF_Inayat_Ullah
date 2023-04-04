# Inayat Ullah
import numpy as np
import pandas as pd
Students = pd.Series(["Inayat","Bakht","Bilal","Inayat","Danish","Bilal","Bilal","Azmat"])
print(Students)
print("------------")

# Indexing 
print("At index zer = ",Students.loc[0])
print("------------")

# List of indexing
print("List indexing = ",Students.loc[[0, 4]])
print("------------")

# Unique repace the duplicate value ir make it unique
uniq = pd.unique(Students)
print("Unique values = ",uniq)
print("----------------")

# will count the number of itmes in the list
count = pd.value_counts(Students)
print("Count_values\n",count)
print("------------")
# Assigning number to the name of students

number = [0,1,2,0]*2
print(Students.take(number))
print("-------------")

# Finding length of the Students 
len = len(Students)
print("Length of Students list = ",len)
print("-------------")

# DataFram
df = pd.DataFrame({'Student': Students,'id': np.arange(len),'count': np.random.randint(1, 8,
    size=len),'weight': np.random.uniform(0, 4, size=len)},
    columns=['id', 'Student', 'count', 'weight'])
print(df)
print("-------------")

# Convert into catgerical data 
student_cat = df['Student'].astype('category')
print(student_cat)
c = student_cat.values
print(c)
print(c.codes)
print("-------------")

# Checking memory usage
print(Students.memory_usage())
print("-------------")

# dummy Variable
df= pd.Series(['a', 'b', 'c', 'd'] , dtype='category')
dum = pd.get_dummies(df)
print(dum)


