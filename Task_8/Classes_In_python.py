#  Inayat Ullah
# Classes in python
print("------------")
class Students:
    Name = "Inayat"
    Roll_No = 52
# Object of that class
obj = Students
print("Name of student is ",obj.Name)
print("------------")

# use of  __init__() function 
class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
obj = person(name="Kashi",age=23)
print("Age of the person is ",obj.age)
print("------------")

# Function in class
class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def Hello(self):
        print("Hello "+self.name)
obj = person(name="Kashi",age=23)
obj.Hello()
print("------------")

# Inheritance in Classes
class Parant:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def Print(self):
    print("Name -->",self.name, "Age -->",self.age)

class child(Parant):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)

x = child("Saeed", 60)
x.Print()
print("------------")