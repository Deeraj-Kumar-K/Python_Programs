# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

# Two Sum II - Input Array Is Sorted
#Given array is already sorted in non-decreasing order
#find two numbers such that they add up to a specific target number
#Return the indices of the two numbers,
#there is exactly one solution. You may not use the same element twice.
'''
Example 1:
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9.
Therefore, index1 = 1, index2 = 2. We return [1, 2].

Example 2:
Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6.
Therefore index1 = 1, index2 = 3. We return [1, 3].
'''

from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1
        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left+1, right+1]
            elif numbers[left] + numbers[right] < target:
                left += 1
            elif numbers[left] + numbers[right] > target:
                right -= 1
        return []


numbers = [2,7,11,15]
target = 9
print(Solution().twoSum(numbers, target))
