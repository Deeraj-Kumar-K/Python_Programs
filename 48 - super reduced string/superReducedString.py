# https://www.hackerrank.com/challenges/reduced-string/problem

# Super Reduced String
#In each operation, select a pair of adjacent letters that match, and delete them.
#Delete as many characters as possible using this method and return the resulting string.
#If the final string is empty, return Empty String
'''
Example:
s = 'aab'
aab shortens to b in one operation: remove the adjacent a characters.

s = 'abba'
Remove the two 'b' characters leaving 'aa'. Remove the two 'a' characters to leave ''. Return 'Empty String'.
'''

def superReducedString(s):
    # Write your code here
    if len(s) == 1:
        return s
        
    res = list(s)
    length = len(res)
    left = 0
    right = 1
    
    while right < length:
        if res[left] == res[right]:
        #delete the right element first
        #if we delete left element 1st 
        #then element in right index will shift to left index
        #i.e. element in index 1 will shift to index 0
            del res[right]
            del res[left]
            length = len(res)
            left = 0
            right = 1
        else:
            left += 1
            right += 1
            
    return "".join(res) if len(res) > 0 else "Empty String"
