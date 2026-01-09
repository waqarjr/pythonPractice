# Ordered (from Python 3.7+)
#  Mutable (can be changed)
#  Keys must be unique
#  Keys must be immutable (string, number, tuple)
#  Values can be any type

student = {
    "name ": "Ahmad",
    "age": 23,
    "para": "Digital Dreams comes to life here ",
    "newStudents": {
        "name ": "Hanzala Habib",
        "age": 23,
        "para": "you have recived a lot of numbers"
    },

    "calculation": 2 + 2,
}
print(student)
# Accessing Values
print(student["name "])
# Using get() (safe way)
print(student.get("city"))        # None
print(student.get("city", "N/A"))  # Default value



for students in student.items():
    print(students)


# CRUD in the dictinary
# create , read , update , delete

person = {"name": "Waqar", "age": 22}
person = dict(name="Waqar", age=22)

# Read
person["age"]
# by get method 
print(person.get("city"))        # None
print(person.get("city", "N/A")) # Default value

# update
person["name"] = "ahmad"
person.update({"age": 25, "country": "Pakistan"})

# Adding and updating 
person["city"] = "Lahore"
# Update existing key
person["age"] = 23


# Delete 
# person.pop("age")       # Removes specific key
# person.popitem()        # Removes last item
# del person["city"]      # Deletes key
# person.clear()          # Removes all items

# person.keys()    # dict_keys
# person.values()  # dict_values
# person.items()   # dict_items

data = {
    "name": "Waqar",
    "age": 22,
    "skills": ["Python", "JS"],
    "address": {"city": "Lahore", "zip": 54000},
    "is_student": True
}
