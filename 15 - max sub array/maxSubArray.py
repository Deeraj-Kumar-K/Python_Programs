# https://leetcode.com/problems/maximum-subarray/

# Maximum Subarray
# Given an integer array, find the contiguous subarray
#(containing at least one number) which has the largest sum
# and return its sum.
# A subarray is a contiguous part of an array.
'''
Example 1:
Input: [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Example 2:
Input: [1]
Output: 1
'''

def maxSubArray(nums):
        #Kadane's Algo of MaxSum
        res = nums[0]
        maxlength = nums[0]
        for i in range(1,len(nums)):
            maxlength = max(maxlength + nums[i], nums[i])
            res = max(maxlength,res)
        return res


array = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(array))
array = [5,4,-1,7,8]
print(maxSubArray(array))
