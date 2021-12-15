# https://leetcode.com/problems/palindrome-number/

# Palindrome Number
#Given an integer x, return true if x is palindrome integer.
#An integer is a palindrome when it reads the same backward as forward.
'''
Example 1:
Input: x = 121
Output: true

Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-.
Therefore it is not a palindrome.
'''

class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x < 0:
            return False
        
        rev = 0
        num = x
        while x > 0:
            rem = x % 10
            rev = rev * 10 + rem
            x = x // 10

        if num == rev:
            return True
        
        return False
