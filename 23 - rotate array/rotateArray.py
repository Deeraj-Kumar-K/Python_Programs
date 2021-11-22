# https://leetcode.com/problems/rotate-array/

# Rotate Array
#Rotate the given array to the right by k steps, where k is non-negative.
'''
Example:
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]

Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
'''

from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:

        length = len(nums)
        array = []
        array.extend(nums)
        if k >= length:
            k = k % length
        
        counter = -k
        for i in range(k):
            nums[i] = array[counter]
            counter += 1
  
        counter = 0
        for j in range(k,length):
            nums[j]=array[counter]
            counter += 1

        return nums   


nums = [1,2,3,4,5,6,7]
k = 3
print("Array:",nums)
print("\nAfter rotating by",k,"steps")
print(Solution().rotate(nums, k))
