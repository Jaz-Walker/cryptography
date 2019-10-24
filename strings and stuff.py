# Strings


# Concatenation
# 2 strings or more and put them together


firstName = "Joe"
lastName = "Mama"

print(firstName + " " + lastName)

name = firstName + " " + lastName
lastFirst = lastName + ", " + firstName

print(lastFirst)

# Repetition

print("Hip "*4 + "Hooray!")

def rowYourBoat():
    print("Row, "*3 + "your boat")
    print("Gently down the stream")
    print("Merrily, "*4)
    print("Life is but a dream")

rowYourBoat()

# Indexing

name = "Roy G Biv"
firstCharacter = name[0] # the brackets allow us to grab certain characters, in this the letter in position 0 (position 0 is the first position)
print(firstCharacter)


middleCharacterIndex = len(name) // 2 # we use this to find the length of out string
print(middleCharacterIndex)
print(name[middleCharacterIndex])


print(name[-1])

for i in range(1, len(name)):
    print(name[i])

# Slicing and dicing


print(name[0:3])

for i in range(0, len(name)+1):
    print(name[0:i])


# searching

print("Biv" in name)