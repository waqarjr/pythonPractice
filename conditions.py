print(bool(10 == 10))
# true
print(bool(10 == "10"))
# false

print(bool("bag" > "apple" and "bag " > "cat"))
print(bool("BAG" > "bag"))

print(ord("B"))
print(ord("b"))

orang = 10
if orang == 10:
    print("success")
else:
    print("Fail")


def add(orang):
    print("Add function ")
    return orang


if (orang > 9):
    newvalue = add(orang)
    print(newvalue)
    print("Condition true")
    #    return orang + 12

ty = "string"
print(type(ty))

age = 10
message = "Eligible" if age >= 18 else print("Not Eligible")
print(message)

# channing comparison operator
channing_operator = 20
if 18 <= channing_operator < 65 :
    print("welcome")

# and or not

condition = True
condition1 = False
student = False

if (condition or condition1) and not student:
    print("good")
else:
    print("bad")
