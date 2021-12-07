# https://leetcode.com/problems/ransom-note/

# Ransom Note
#Given two stings ransomNote and magazine,
#return true if ransomNote can be constructed from magazine and false otherwise.
#Each letter in magazine can only be used once in ransomNote.
'''
Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:
Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:
Input: ransomNote = "aa", magazine = "aab"
Output: true
'''

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        allLetters = collections.Counter(magazine)
        for i in range(len(ransomNote)):
            if ransomNote[i] in allLetters:
                if allLetters[ransomNote[i]]<=0:
                    return False
                else:
                    allLetters[ransomNote[i]] -=1
            else:
                return False
        return True
                
