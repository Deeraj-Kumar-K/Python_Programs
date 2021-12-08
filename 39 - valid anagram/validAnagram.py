# https://leetcode.com/problems/valid-anagram/

# Valid Anagram
#Given two strings s and t, return true if t is an anagram of s.
#Anagram is a word or phrase that's formed by rearranging the letters of another word or phrase.
'''
Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashTable = collections.Counter(s)
        for i in range(len(t)):
            if t[i] in hashTable:
                if hashTable[t[i]] > 0:
                    hashTable[t[i]] -= 1
                else:
                    return False
            else:
                return False
        return True
