# Caesar Cipher Encryptor
# Given a string and an integer value,
# Shift every letter/character in the sring by given value
# Ex: String='abc' , key=1 , Output='bcd'
# Ex: String='xyz' , key=2 , Output='zab'

# Time: O(n) , Space: O(n)
# where n is the length of input string

def caesarCipherEncryptor(string, key):
    newLetters = []
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    # for large key value, mod by 26 (26 alphabets)
    newKey = key % 26
    for letter in string:
        newLetters.append(getNewLetter(letter,newKey,alphabet))
    return "".join(newLetters)

def getNewLetter(letter, key, alphabet):
    # generate newLetterCode nLC
    nLC = alphabet.index(letter) + key
    # get index value of current letter from alphabet array
    # unicode of letter 'a'=97 and 'z'=122
    return alphabet[nLC] if nLC <= 25 else alphabet[-1 + nLC % 25]
    # we mod by 25 because array index starts from zero


string = "zab"
key = 27 # (27 % 26) = '1' therefore, newKey = 1
print("String:",string)
print("Key:",key)
print("Output:",caesarCipherEncryptor(string, key))
