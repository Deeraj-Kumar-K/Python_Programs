# Palindrome Check
# Same if read from left or right
# Ex: abbba - palindrome
# Ex: fgh - not palindrome
'''
# Solution 1: Using Recursive approach
# recursion happens n/2 times which is O(n) time
# and O(n) space for call stack
# Time: O(n) , Space: O(n)

def palindromeCheck(string, i=0):
    j = len(string)-1-i
    return True if i>=j else string[i]==string[j] and palindromeCheck(string,i+1)
'''

# Solution 2: Using tail recursion
# tail recursion when recursive function as last statement of the function
# uses few stack frames, consumes less memory
# Time: O(n) , Space: O(n)

def palindromeCheck(string, i=0):
    j = len(string)-1-i
    if i >= j:
        return True
    if string[i] != string[j]:
        return False
    return palindromeCheck(string, i+1)


string = "12321"
print("String:",string)
print("Is palindrome:",palindromeCheck(string))

string = "4567"
print("\nString:",string)
print("Is palindrome:",palindromeCheck(string))
