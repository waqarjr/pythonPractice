fruits = ["apple", "grapes", "loop", "happy"]

for number in range(len(fruits)):
    print("Iiteration", number + 1,  (number + 1) * ".")

for number in range(0, 10, 2):
    print(number, number * "*")


# for else loop
success = True
for number in range(4):
    print("Accepted")
    if success:
        break
        # continue
    else:
        print(number)
else:
    print("Accepted & Fail")

# nested loop
for x in range(3):
    for y in range(3):
        print(f"({x} : {y})")


obj = {"name": "Waqar", "class": "BSCS", "age": 12, "adult": True}


for key, value in obj.items():
    print(f"Object keys {key} values {value}")

print(len(obj), "object")

# iteration
# string
for string in "phyton":
    print(string)

# array
for array in [1, 2, 3, 4]:
    print(array)

# while loop
number = 100
while number > 0:
    print(number)
    number //= 2

comment = ""

while comment != "quit":
    print()
