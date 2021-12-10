# https://leetcode.com/problems/hamming-distance/

# Hamming Distance
#The Hamming distance between two integers is the number of positions
#at which the corresponding bits are different.
#Given two integers x and y, return the Hamming distance between them.
'''
Example:
Input: x = 1, y = 4
Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑
The above arrows point to positions where the corresponding bits are different.
'''

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        #xor gives output '1' when bits are different
        Xor = str(bin(x ^ y))
        return(Xor.count('1'))
