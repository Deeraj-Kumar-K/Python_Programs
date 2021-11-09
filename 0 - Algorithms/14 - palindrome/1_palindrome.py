# Palindrome Check
# Same if read from left or right
# Ex: abbba - palindrome
# Ex: fgh - not palindrome
'''
# Solution 1: By creating new String
# Time: O(n^2) , Space: O(n)
# to add new character, it creates new string and iterates through it

def palindromeCheck(string):
    newString = ""
    for i in reversed(range(len(string))):
        newString += string[i]
    return string == newString
'''

# Solution 2 : By creating a List
# Time: O(n), Space: O(n)

def palindromeCheck(string):
    newStr = []
    for i in reversed(range(len(string))):
        newStr.append(string[i])
    return "".join(newStr) == string


string = "abbba"
print("String:",string)
print("Is palindrome:",palindromeCheck(string))

string = "fgh"
print("\nString:",string)
print("Is palindrome:",palindromeCheck(string))
