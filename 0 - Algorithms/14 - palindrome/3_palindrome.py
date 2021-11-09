# Palindrome Check
# Same if read from left or right
# Ex: abbba - palindrome
# Ex: fgh - not palindrome

# Solution : Using Two Pointers (Iterative approach)
# Time: O(n) , Space: O(1)

def palindromeCheck(string):
    left = 0
    right = len(string)-1
    while left < right:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1
    return True


string = "daaad"
print("String:",string)
print("Is palindrome:",palindromeCheck(string))

string = "now"
print("\nString:",string)
print("Is palindrome:",palindromeCheck(string))
