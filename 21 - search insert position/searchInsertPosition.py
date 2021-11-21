# https://leetcode.com/problems/search-insert-position/

# Search Insert Position
#Given sorted array of distinct integers and a target value,
#return the index if the target is found. If not found then,
#return the index where it would be if it were inserted in order.
'''
Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:
Input: nums = [1], target = 0
Output: 0
'''

from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # idx denotes index value
        idx = 0
        #if target is found, return index value
        if target in nums:
            for num in nums:
                if num == target:
                    return idx
                else:
                    idx+=1
        #if not found, return index where it would be if inserted
        else:
            for num in nums:
                if num < target:
                    idx += 1
            return idx

nums = [1,3,5,6]; target = 5;
print("Input: nums =",nums,", target = ",target)
print("Output:",Solution().searchInsert(nums, target))

nums, target = [1], 0
print("Input: nums =",nums,", target = ",target)
print("Output:",Solution().searchInsert(nums, target))

