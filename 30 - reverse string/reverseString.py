# https://leetcode.com/problems/reverse-string/

# Reverse String
#Write a function that reverses a string
#The input string is given as an array of characters s
#Do this by modifying input array in-place with O(1) extra memory.
'''
Example:
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
'''
from typing import List
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s)-1

        while left < right:
            temp = s[left]
            s[left] = s[right]
            s[right] = temp
            left += 1
            right -= 1
        return s

s = ["h","e","l","l","o"]
print(Solution().reverseString(s))
