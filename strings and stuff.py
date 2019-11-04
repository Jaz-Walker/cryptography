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

# string methods
    # Method        Use Example         Explanation
    # center        aStr.center(w)      Finds the center to whatever you put into parentheses with the (w) being a different word or phrase
    # ljust         aStr.ljust(w)       Python string method ljust() returns the string left justified in a string of length width.
    # rjust         aStr.rjust(w)       Returns the string right justified in a string of length width.
    # upper         aStr.upper()        Returns the uppercased string from the given string.
    # lower         aStr.lower()        Returns the lowercased string from the given string.
    # index         aStr.index(item)    Searches for given element from start of the list and returns the lowest index where the element appears.
    # rindex        aStr.rindex(item)   Returns the last index where the substring str is found, or raises an exception if no such index exists.
    # find          aStr.find(item)     If substring exists inside the string, it returns the index of first occurence of the substring. If substring doesn't exist inside the string, it returns -1.
    # rfind         aStr.rfind(item)    Returns the highest index of the substring if found in given string. If not found then it returns -1.
    # replace       aStr.replace(old, new)       Returns a copy of the string where all occurrences of a substring is replaced with another substring.


# searching

print("Biv" in name)


# character functions

print(ord('a'))

print(chr(69))

from mapper import *
print(indexToLetter(24))


from crypto import *

print(scrambleEncrypt("THE MEETING IS AT FIVE OCLOCK"))

print(scramble2Decrypt("H ETN SA IEOLCTEMEIGI TFV COK"))


alphabet = "abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ.,?!"

def cesar(word):
    encrypt = ""
    for ch in word:
        Letters = alphabet.find(ch)
        nextLetters = (Letters + 3) % 57
        encrypt += alphabet[nextLetters]
    return encrypt


print(cesar("My name is Jaz."))

def decrypt(encrypt):
    translate = ""
    for ch in encrypt:
        Letters = alphabet.find(ch)
        pastLetters = (Letters - 3) % 57
        translate += alphabet[pastLetters]
    return translate


print(decrypt("PACqdphClvCMdB"))

