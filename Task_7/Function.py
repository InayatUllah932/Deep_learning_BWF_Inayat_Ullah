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

print("---------")
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
n = int(input("Enter Any number you want! "))
print(num(n))
print("---------")
