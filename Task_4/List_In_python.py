# Inayat Ullah
# let num be the list

num = [1,4,2,7,5,100,60,50,100]
# I will practice on indixing
print("First Element Of list is ",num[0])
# You can perform add through indixing 

print(num[4] + num[6])

# How to add new element to the list 

num.append(45)
num[0] = 67
num[5] -=20

# We can remove element from the list
num.remove(num[7])

print(num)
print("--------")
print("Sorting of list")
num.sort()
print(num)

print("--------")
print("Sorting of list in decending order")
num.sort(reverse=True)
print(num)

print("--------")
# For loop over list
for i in num:
    print(i)
print("--------")
# We can also write this loop
for i in range(len(num)):
    print(num[i])
print("--------")
#While loop over list
v = 0
while v < len(num):
    print(num[v])
    v+=1
print("--------")
v = 0
while True:
    if v < 5:
        print(num[v])
        v+=1



