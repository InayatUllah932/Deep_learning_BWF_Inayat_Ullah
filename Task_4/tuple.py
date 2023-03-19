#       Inayat Ullah
# Tuple in pytho
Tuple = ("Inayat","Kashi","Bila","Samreen")
print(Tuple)
print(type(Tuple))
# Tuple is unchangeable mean once you create the tuple items insde can not be change 
#The mean difference between list and tuple is that list can be change but tuple can not

#Indexing in tuple

print(Tuple[0])
print("----------")
 # Loop in tuple
for i in Tuple:
    print(i)

print("----------")
#String ,Int and boolean
Tuple_2 = ("Name",34,"Email",True,False)
print("Tuple which has string, int and boolean = ",Tuple_2)

print("----------")
#Updating tuple in python we will change ffirst tuple into listt and than we will convert from list int tuple
num = list(Tuple_2)
num[0] = "Roll_No"
num = tuple(num)
print(num)
print("----------")