# Caesar Cipher Encryptor
# Given a string and an integer value,
# Shift every letter/character in the sring by given value
# Ex: String='abc' , key=1 , Output='bcd'
# Ex: String='xyz' , key=2 , Output='zab'

# Time: O(n) , Space: O(n)
# where n is the length of input string

def caesarCipherEncryptor(string, key):
    newLetters = []
    # for large key values, mod by 26 (26 alphabets)
    newKey = key % 26
    for letter in string:
        newLetters.append(getNewLetter(letter,newKey))
    return "".join(newLetters)

def getNewLetter(letter, key):
    # generate newLetterCode nLC
    nLC = ord(letter) + key
    # ord() returns unicode/ASCII value
    # unicode of letter 'a'=97 and 'z'=122
    return chr(nLC) if nLC <= 122 else chr(96 + nLC % 122)


string = "xyz"
key = 2
print("String:",string)
print("Key:",key)
print("Output:",caesarCipherEncryptor(string, key))
