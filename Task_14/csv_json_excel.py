import pandas as pd
import csv
df = pd.read_csv("data.csv")
print(df)
print("--------------")

# Print the first 5 row in the file
print(df.head(5))
print("--------------")
# Indexing in the file
js = pd.read_json("data.json")
print("Json file =",js)
print("--------------")

# Json first five rows
print(js.head(5))
print("--------------")

# get excel file in python

excel = pd.read_excel("file.xlsx")
print(excel)