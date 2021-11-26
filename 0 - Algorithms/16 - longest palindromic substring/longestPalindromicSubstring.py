# Longest Palindromic Substring
#Given a string s, return the longest palindromic substring in s.
'''
Example 1:
Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"

Example 3:
Input: s = "a"
Output: "a"
'''

#Time and Space Complexity
# Time: O(n) , Space: O(1)
# where n is the length of input string
    
class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        # to find palindromic substring
        def getLongestPalindrome(s, left, right):
            while left >= 0 and right < len(s):
                if s[left] != s[right]:
                    break
                left -= 1
                right += 1
            #we return (left+1) but not (right-1)
            #coz right value is excluded during string slicing
            return [left + 1 , right]
            #also, for Ex: "gg", if we do left+1 and right-1 here
            #then left and right values will cross each other
            #causing left=1 and right=0, which gives error
        
        # to find longest palindromic substring
        # instead of storing substring, we store index values
        currentLongest = [0, 1]
        #we take [0, 1], where 1 is excluded while string slicing
        for i in range(1,len(s)):
            #odd substring, Ex: aba 
            odd = getLongestPalindrome(s, i-1, i+1)
            #even substring, Ex: abba
            even = getLongestPalindrome(s, i-1, i)
            
            #find longest substring by subtracting index values to find length
            #longest = max(odd, even, key = lambda x: x[1] - x[0])
            #we can use lambda function also as written in above line
            if odd[1]-odd[0] > even[1]-even[0]:
                longest = odd
            else:
                longest = even

            #above method can be applied for currentLongest also
            #if longest[1] - longest[0] > currentLongest[1] - currentLongest[0]:
            #    currentLongest = longest
            currentLongest = max(longest, currentLongest, key = lambda x: x[1] - x[0])
            
        #return longest palindromic substring using string slicing
        return s[currentLongest[0] : currentLongest[1]]
    

s = "abayyzyyj"
print(Solution().longestPalindrome(s))
