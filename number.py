import math

print(2 + 2)
print(2 - 2)
print(2 * 7)
print(10 / 3)
print(10 // 3)
print(10 % 3)
print(3 ** 3)

print(round(2.9))
print(abs(-2.9))

math.ceil(2.2)

# conditions of booleans
print(bool(0))
print(bool("False"))
print(bool([]))
print(bool(False))
print(bool(None))
# by defaul input filed takes a string not number or other but we can convert into by str()



input = input("Enter your value : ")
y = int(input) + 1
print(y)



x = 10
y = "hello"
z = 3.5

print(isinstance(x, int))    # True
print(isinstance(y, str))    # True
print(isinstance(z, float))  # True
