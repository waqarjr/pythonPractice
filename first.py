print("Hello ! ")
print("*" * 10)
age = 18

if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible")

fruits = ["apple", "banana", "mango"]

for fruit in fruits:
    print(fruit)

for i in range(5):
    print(i)

condition = False
condition = True
print(condition)

waqar_ahmad = "waqar"
print(waqar_ahmad)

education = """ 
Welcome to the world of education 

Whh
"""
print(education)

# len() function use case : Basically we use this for to return the number of items of an objects 

numbers = [10, 20, 30, 40]
print(len(numbers))

name = "Python"
print(len(name))

# len() with tuple
data = (1, 2, 3)
print(len(data))

# len() with dictionary
user = {
    "name": "Waqar",
    "age": 25,
    "city": "Lahore"
}
print(len(user))
names = ["Ali", "Waqar", "Ahmed"]

for i in range(len(names)):
    print(i, names[i])


# List in Python
# What is a List?
# Ordered collection
# Mutable (can change)
# Allows duplicate values
# Written using []

fruits = ["apple", "banana", "mango"]
print(fruits)

hun = 10
num = hun

num = 20 

print(hun)
print(num)


import math 
# alies
import math as m 

# 
from math import sqrt , log
print(int(math.sqrt(4)))
print(int(m.sqrt(4)))
print(sqrt(10))
print(log(10))
