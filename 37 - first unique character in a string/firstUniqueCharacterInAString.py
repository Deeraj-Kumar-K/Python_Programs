# https://leetcode.com/problems/first-unique-character-in-a-string/

# First Unique Character in a String
#Given string, find first non-repeating character in it
#and return its index. If it does not exist, return -1.
'''
Example 1:
Input: s = "leetcode"
Output: 0

Example 2:
Input: s = "loveleetcode"
Output: 2

Example 3:
Input: s = "aabb"
Output: -1
'''

class Solution:
    def firstUniqChar(self, s: str) -> int:
        '''
        Solution - 1
        dct=collections.Counter(s)
        for i,el in enumerate(s):
            if dct[el]==1: 
                return i
        return -1
        '''
        
        # Solution - 2
        hashTable = {}
        for letter in s:
            if letter in hashTable:
                hashTable[letter] += 1
            else:
                hashTable[letter] = 1
            
        for idx in range(len(s)):
            if hashTable[s[idx]] == 1:
                return idx
        return -1
        

s = "loveleetcode"
print(Solution().firstUniqChar(s))
