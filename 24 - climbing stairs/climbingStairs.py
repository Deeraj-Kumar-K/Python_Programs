# https://leetcode.com/problems/climbing-stairs/

# Climbing Stairs
#You are climbing a staircase. It takes n steps to reach the top.
#Each time you can either climb 1 or 2 steps.
#In how many distinct ways can you climb to the top?
'''
Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

For climbing,
0 stairs = 1 way
1 stairs = 1 way
2 stairs = 2 ways
3 stairs = 3 ways
4 stairs = 5 ways [1111, 112, 121, 211, 22] 
It is creating a fibonacci series 1 1 2 3 5....
'''

class Solution:
    def climbStairs(self, n: int) -> int:
        
        #Using Fibonacci logic
        arr = []
        
        #for climbing 0 stairs, 1 way
        arr.append(1)
        
        #for climbing 1 stairs, 1 way
        arr.append(1)
        
        #for climbing stairs from 2 stairs to n
        for i in range(2, n+1):
            arr.append(arr[i-1] + arr[i-2])
            
        return arr[n]


print(Solution().climbStairs(3))
