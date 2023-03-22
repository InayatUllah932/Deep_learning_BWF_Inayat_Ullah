# Inayat Ullah
#Check the number is divisible by 2 or not?

print("---------")
num = [1,2,3,4,5,6,7,8]
for i in num:
    if i % 2==0:
        print(i,"is divisible by 2")
    else:
        print(i,"is not divisible by 2")

print("---------")
num_1 = 5 
num_2 = 6
if num_1 > num_2:
    print(num_1," greater then ",num_2)
else:
    print(num_2," greater then ",num_1)

print("---------")
# Checking number in the list
list = [1,4,3,7,5,9,7,0]
print("List = [1,4,3,7,5,9,7,0]")
#check 2 is present in the list or not
if 2 in list:
    print(2,"print in the list")
else:
    print(2,"Is not present in the list")

print("---------")
A = 23
B = 45
C = 10
if B > A and C < B:
    print(B,"Is greater then both ",A,"and", C)
else:
    print("Condition is not satisfy")
print("---------")


