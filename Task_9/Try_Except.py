                             # Inayat Ullah

'''
The try block lets you test a block of code for errors.
The except block lets you handle the error.
The else block lets you execute code when there is no error.
The finally block lets you execute code, regardless of the result of the try- and except blocks.
'''
# When there is no error in the file try section will give result in the output
print("---------------")
try:
    print("There is no error in the file")
except:
    print("Exceptional error In Code")


print("---------------")
# When there is error in the file Except section will print in output
x = 3
try:
    print(x/0)
except:
    print("You can't divid by 0")


print("---------------")
# handling file through try except 
try:
    with open("FileName") as file:
        cont = file.read()
        print("File Exist")
except:
    print("File Not Exist")


print("---------------")
# Finally statment in try exception

try:
    print("Output of try section")
except:
    print("Error")
finally:
    print("Finally statment print --> try except statment complete")

    
print("---------------")

