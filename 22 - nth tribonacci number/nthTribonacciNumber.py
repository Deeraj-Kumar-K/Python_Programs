# https://leetcode.com/problems/n-th-tribonacci-number/

# N-th Tribonacci Number
#The Tribonacci sequence Tn is defined as follows: 
#T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
#Given n, return the value of Tn.
'''
Example:
Input: n = 4
Output: 4

Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4
'''

class Solution:
    def tribonacci(self, n: int) -> int:
        t1,t2,t3=0,1,1
        if n<3:
            return [0,1,1][n]
        for i in range(2,n):
            t1,t2,t3=t2,t3,t1+t2+t3
        return t3


print(Solution().tribonacci(4))
