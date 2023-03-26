# Inayat
# Function without passing parameters
print("---------")
def Student():
    FirstName = "Inayat"
    LastName = "Ullah"
    Age = 22
    return (FirstName,LastName,Age)
print(Student())

print("---------")
# Passing parameters in function
def Student(num):
    if num >= 10:
        print("Hi user You pass the critira WELCOME!")
    else:
        print("You faile in this course!")
x = 18
Student(x)

print("---------")
# Docstring In Python
def sum(x,y):
    '''
    This function print the sum of x and y
    '''
    print("x + y = ",x+y)
x = 3
y = 7
sum(x,y)
print(sum.__doc__)

print("---------")
# Docstring Practing
def Docs():
    '''
            {Docstring} 
    Hi Take the square of number in python
        squar = number**2
            then divid it by 2
            final = sqaur / 2
    '''
print(Docs.__doc__)

# Return in python
print("---------")
def Get_Full_Name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()
print(Get_Full_Name('inayat', 'ullah'))

print("------------------")
# Return in python
def Squar(num):
    return (num**2)
num = 5
print(Squar(num))

print("---------")
def num(n):
    if n > 0:
        if n < 10:
            return True
        else:
            return("Greater then 10")
    else:
        return False
n = 11
print(num(n))

print("---------")
def number(num,num1):
    if num > num1:
        return num
    else:
        print("Ho",num1)
        return num1
        #print("Ho")
def Helloo(num2):
    num3 = number(2,3)
    sum1 = num2 + num3
    return sum1
num2 = 7

print(Helloo(num2))
print("---------")

# A default function for addition  
def Adding(a):  
    # Nested function with second number   
    def Addition(b):   
            return a + b # addition of two numbers  
    return Addition # Result  
  
# Taking both number variable as user input  
a = 4  
b = 5 
# Assigning nested adding function to a variable  
AddVariable = Adding(a)  
# Using variable as high order function  
Result = AddVariable(b)  
# Printing result  
print("Sum of Two numbers given by you is: ", Result)  

# Use of title built in function 
print("---------")
def user(username):
 print("Hello, " + username.title() + "!")
user('inaYat')

# Function that retrun My info in dict form
print("---------")
def My(first_name, last_name, age=''):
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person
musician = My('Inayat', 'Ullah', age=23)
print(musician)

# Function that return city and Country
print("---------")
def city_country(City,Country):
    Info = City+" , "+Country
    return Info.title()
num = city_country("wana","pakistan")
print(num)

print("---------")
un = ['iphone case', 'robot pendant', 'dodecahedron']
while len(un)>0:
    un = un.pop()