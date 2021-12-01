# https://leetcode.com/problems/house-robber/

# House Robber
#Adjacent houses have security systems connected and it will automatically
#contact the police if two adjacent houses were broken into on the same night.
#Given an array representing the amount of money of each house,
#return maximum amount of money you can rob without alerting the police.
'''
Example 1:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 2:
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
'''
from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        # [rob1, rob2, n, n+1, ......]
        for n in nums:
            newRob = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = newRob
        return rob2
        
        '''
        #create new list of length(nums),initialize all elements with '0'
        dp = [0] * len(nums)
        
        if len(nums) == 1:
            return nums[0]
        if len(nums) ==2 :
            return max(nums)
        
        dp[0] = nums[0]
        dp[1] = nums[1]
        for i in range(2,len(nums)):
            dp[i] = max(dp[:i-1]) + nums[i] 
            # (i-1)th element is excluded i.e adacent houses
        return max(dp)
        '''
nums = [1,2,3,1]
print(Solution().rob(nums))
