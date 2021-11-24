# https://leetcode.com/problems/move-zeroes/

# Move Zeroes
#Given an integer array, move all 0's to the end of it
#while maintaining the relative order of the non-zero elements.
#Note that you must do this in-place without making a copy of the array.
'''
Example 1:
Input: nums = [0,1,0,5,16]
Output: [1,5,16,0,0]

Example 2:
Input: nums = [0]
Output: [0]
'''

from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        k = 0
        for i in range(len(nums)):
            if nums[k] == 0:
                del nums[k]
                nums.append(0)
            else:
                k += 1
        return nums


arr = [0,1,0,5,16]
print(Solution().moveZeroes(arr))
    
