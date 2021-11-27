# https://leetcode.com/problems/product-of-array-except-self/

# Product of Array Except Self
#Given integer array nums, return an array answer such that
#answer[i] is equal to the product of all the elements of nums except nums[i].
#product of any prefix/suffix of nums will fit in a 32-bit integer.
#Solve in O(n) time and without using the division operation.
'''
Example:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Input :  [1, 2, 3, 4]
After prefix,
Result: [1, 1, 2, 6]
here, element '4' of input array is ignored
last element of result array,'6' is in its correct place

After postfix,
Result: [24, 12, 8, 6]        
'''     
from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # Solution without using extra memory
        #(The output array does not count as extra space)
  
        res = [1] * len(nums)
        
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
            
        return res

arr = [1,2,3,4]
print(Solution().productExceptSelf(arr))   
