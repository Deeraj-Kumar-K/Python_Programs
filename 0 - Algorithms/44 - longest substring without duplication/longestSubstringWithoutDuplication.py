# Longest Substring Without Duplication

# Given a string, return its longest substring without duplicate characters.
'''
Explanation:

string = "abcdeabcdefabc"
here, we have three strings without duplicate characters,
"abcde" - length '5', "abcdef" - length '6' and "abc" - length '3'
The longest substring without duplication is of length '6'
Output = "abcdef"


# Time and Space Complexity:

We iterate through the string of length 'n', that is O(n) time.

# O(min(n, a)) space because we might store all 'n' characters in hashtable
if all characters in the string were unqiue. But if we have duplicate
characters, we only store 'a' characters in hashtable,
where 'a' is the length of all unique characters.

'''

# O(n) time , O(min(n, a)) space
# where 'n' is length of string and 'a' is the length of all unique characters

def longestSubstringWithoutDuplication(string):
    lastSeenAt = {} # hashtable stores characters and their last seen index
    longest = [0, 1]
    startIdx = 0
    for idx, char in enumerate(string): # each character is given index values
        if char in lastSeenAt: # if currentChar is a duplicate character
            startIdx = max(startIdx, lastSeenAt[char] + 1)

        if longest[1] - longest[0] < idx + 1 - startIdx: # update longest string
            longest = [startIdx, idx + 1]

        lastSeenAt[char] = idx # update last seen index value of currentChar

    return string[longest[0] : longest[1]]
    

# Input
string = "abcdeabcdefabc"
print("String =", string)
print("Output =", longestSubstringWithoutDuplication(string))
# Output = abcdef
