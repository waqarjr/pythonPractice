const = "python programming"
print(len(const))
# start of the string
print(const[0])
# end of the string
print(const[-1])
# split the string
print(const[0:3])
# for to get the string same as well
print(const[0:])
# will give the first 3 character
print(const[:4])
# copy of the string
print(const[:])
# this will remove the first and last of the string 
print(const[1:-1])
# in this way we can write buddlequotation
# here \ is a escape sequence if we use
# \" this  will  single dubble quote in return "
# \' smae like above
# \\  in return this will give me \
# \n for the next line of the code

nextline = "next \n line"
print(nextline)

string = 'welcome "World"'
print(string)

string1 = ' welcome \" world'
print(string1)

number = 10
# we use f for the template litteral
doubleString = f'welcome "world " {number}'
print(doubleString)

# contcatination
# here also + button is used for concatination
first = "waqar"
second = "ahmad"
full = first + second
fullSecond = first + " " + second
fullThird = f"{len(first)}  {2 + 3}"

print(full)
print(fullSecond)
print(fullThird);

# dot notation methods in the python
notation = "dot notation"
# this will give us a index
finding = notation.find("t")
print(finding);

# this will always return boolean 
print( "dot" in notation);
print ("pro" not in notation);

print(notation.capitalize());