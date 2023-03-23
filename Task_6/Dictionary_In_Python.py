# Inayat Ullah
print("----------")
Dict = {"Name":"Inayat","Roll_No":52,"Email":"Anayat2019@namal.edu.pk"}
print(Dict)
print("----------")

# Add in Element into the dictionary
Dict["Department"] = "Computer Science"
print(Dict)
print("----------")

# Updating Dict
Dict["Name"] = "Anayat Ullah"
print(Dict["Name"])
print("----------")

# Removing Item from the dictionary 
Dict.pop("Email")
print(Dict)
print("----------")

# Dictionary which contain string integer and boolean
Dict = {"Institute":"Namal","year":2010,"top_20":True}
if Dict["year"] == 2010 and Dict["top_20"]==True:
    print("Namal Institute is in tope 20 ")
else:
    print("False")
print("----------")

# Dictionary Key sentance
print("Dictionary Key are = ",Dict.keys())
print("----------")
# Dictionary values
print("Dictionary values are = ",Dict.values())
print("----------")


