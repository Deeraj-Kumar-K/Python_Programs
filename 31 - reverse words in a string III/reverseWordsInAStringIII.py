# https://leetcode.com/problems/reverse-words-in-a-string-iii/

# Reverse Words in a String III
#reverse the order of characters in each word within a sentence
#while still preserving whitespace and initial word order.
'''
Example:
Input: s = "God Ding"
Output: "doG gniD"
'''

class Solution:
    
    def reverseWords(self, s: str) -> str:
        
        #Oneliner answer
        #return " ".join(["".join(char[::-1]) for char in s.split(" ")])
        
        allWords = s.split()
        for i in range(len(allWords)):
            singleWord = list(allWords[i])
            allWords[i] = "".join(singleWord[::-1])
        return " ".join(allWords)
    
    
    '''
    #Below is elaborated answer
    
    # function to convert string into list of characters
    def makeList(self,string):
        ans = []
        for i in range(len(string)):
            ans.append(string[i])
        return ans
    
    # function to reverse list of characters
    def reverseString(self,string):
        s = self.makeList(string)
        left = 0
        right = len(s)-1
        while left < right:
            temp = s[left]
            s[left] = s[right]
            s[right] = temp
            left += 1
            right -= 1
        return s
    
    # function to reverse all words in a sentence
    def reverseWords(self, s: str) -> str:
        result = ""
        s = s.split(" ")
        for i in range(len(s)):
            s[i] = self.reverseString(s[i])
            result += "".join(s[i]) + ' '
        return result.strip()
    '''
        
s = "God Ding"
print(Solution().reverseWords(s))
