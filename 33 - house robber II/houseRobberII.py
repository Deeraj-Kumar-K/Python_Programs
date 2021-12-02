# https://leetcode.com/problems/house-robber-ii/

# House Robber II
#All houses at this place are arranged in a circle.
#That means the first house is the neighbor of the last one.
#it will automatically contact the police if two adjacent houses
#were broken into on the same night.
#Given integer array representing the amount of money of each house,
#return the maximum amount of money you can rob without alerting police.
'''
Example 1:
Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then
rob house 3 (money = 2), because they are adjacent houses.

Example 2:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
'''
from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))
    
    def helper(self, nums):
        rob1, rob2 = 0, 0
        for val in nums:
            newRob = max(rob1 + val, rob2)
            rob1 = rob2
            rob2 = newRob
        return rob2

nums = [1,2,3,1]
print(Solution().rob(nums))
