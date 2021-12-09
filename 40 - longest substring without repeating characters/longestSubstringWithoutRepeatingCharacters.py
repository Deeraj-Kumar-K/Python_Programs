# https://leetcode.com/problems/longest-substring-without-repeating-characters/

# Longest Substring Without Repeating Characters
#Given string, find length of the longest substring without repeating characters.
'''
Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that answer must be a substring, "pwke" is a subsequence and not a substring.
'''

class Solution:
    def lengthOfLongestSubstring(self, a: str) -> int:
        length = 0
        maxLength = 0
        hashTable = {}
        s = list(a)
        i = 0
        while i < len(s):
            if s[i] in hashTable:
                if maxLength < length:
                    maxLength = length
                length = -1
                i = hashTable[s[i]]
                hashTable = {}
            else:
                hashTable[s[i]] = i
                
            length += 1    
            if maxLength < length:
                maxLength = length
            i+=1
                
        return maxLength
