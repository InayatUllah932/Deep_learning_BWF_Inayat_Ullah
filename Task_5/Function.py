# Inayat Ullah
print("---------")
# Defining Function
def First_fun():
    print("Hello First_fun")
#Calling function
First_fun()

print("---------")
#Second function
def second_fun():
    A = 3
    B = 5
    print("Sum of A and B =",A+B)
second_fun()

print("---------")
#Function with paramaters
def fun(num_1,num_2):
    print("Hello "+num_1+" "+num_2+" kider hain?")
num_1 = "Inayat"
num_2 = "Rema"
fun(num_1,num_2)
print("---------")

#Function with Unknown parameters
def Unkown(*Student):
    print("Name of the student is ",Student[0])
Unkown("Inayat",52,"Namal Institute")

print("---------")
# Default parameter value
def Namal(Name = "Inayat"):
    print("The name of student is ",Name)
Namal("Bilal")
Namal("Kashif")
Namal("Danish")

print("---------")
#Return statment in function
def number(num):
    return num*5
print(number(5))
print("---------")