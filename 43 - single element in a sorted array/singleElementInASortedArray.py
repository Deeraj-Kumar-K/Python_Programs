# https://leetcode.com/problems/single-element-in-a-sorted-array/

# Single Element in a Sorted Array
#Given a sorted array consisting of only integers where every element appears exactly twice,
#except for one element which appears exactly once.
#Return the single element that appears only once.
#Your solution must run in O(log n) time and O(1) space.
'''
Example 1:
Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2

Example 2:
Input: nums = [3,3,7,7,10,11,11]
Output: 10
'''

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        #if left and right pointer overlap, break the loop, answer found
        while left < right:
            #calculate mid value, preventing overflow of memory
            mid = left + (right - left) // 2
            #check if left and right halves from mid are even or not
            halves_are_even = (right - mid) % 2 == 0
            #if pair is found in right element
            if nums[mid] == nums[mid + 1]:
                # and if halves are even
                if halves_are_even:
                    left = mid + 2  
                else:
                    #if halves are odd
                    right = mid - 1
                    
            #if pair is found in left element
            elif nums[mid] == nums[mid - 1]:
                # and if halves are even
                if halves_are_even:
                    right = mid - 2
                else:
                    #if halves are odd
                    left = mid + 1
                    
            else:      
            #if pair not found, return mid element
                return nums[mid]
        
        #if loop breaks, answer found, return left or right element
        return nums[left]
