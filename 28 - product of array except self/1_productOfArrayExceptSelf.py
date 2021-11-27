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

Solution Explanation
Input :  [1, 2, 3, 4]
Prefix:  [1, 2, 6, 24] - multipying each input first to last element
Postfix: [24, 24, 12, 4] - multipying each input last to first element
                        and storing in reverse order
Result:  [24, 12, 8, 6] - for i-th element, res = prefix(i-1) * postfix(i+1)
prefix(i-1) * postfix(i+1) - this doesnt work for 1st and last element
'''     
from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        #Using extra space for prefix and postfix array
        length = len(nums)
        result = [1] * length
        prefix = [1] * length
        postfix = [1] * length
        
        if length == 2:
            result[0] = nums[1]
            result[1] = nums[0]
            return result
        
        pre = 1
        for i in range(length):
            pre *= nums[i]
            prefix[i] = pre
             
        post = 1
        for j in range(length-1, -1, -1):
            post *= nums[j]
            postfix[j] = post  
         
        res = postfix[1]
        result[0] = res
        for k in range(1,length-1):
            res = prefix[k-1] * postfix[k+1]
            result[k] = res  
        result[length-1] = prefix[length-2]
        
        return result

arr = [1,2,3,4]
print(Solution().productExceptSelf(arr))   
