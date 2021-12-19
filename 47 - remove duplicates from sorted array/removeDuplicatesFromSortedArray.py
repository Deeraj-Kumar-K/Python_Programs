# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

# Remove Duplicates from Sorted Array
#Remove the duplicates in-place such that each unique element appears only once.
#The relative order of the elements should be kept the same.
'''
Example 1:
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2.
It does not matter what you leave beyond the returned k (hence they are underscores).

Example 2:
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Function should return k = 5, with first five elements of nums being 0, 1, 2, 3, and 4.
It does not matter what you leave beyond the returned k (hence they are underscores).
'''

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        '''
        # Solution - 0 (a)
        hashTable = {}
        length = len(nums)
        i = 0
        while i < length:
            if nums[i] not in hashTable:
                hashTable[nums[i]] = True
                #nums.append(nums[i])
                i+=1
            else:
                del nums[i]
            length = len(nums)
            '''
        # Solution - 0 (b) 
        i, j = 0, 0
        length = len(nums)
        while i < length-1:
            j = i+1
            while j < length:
                if nums[i] == nums[j]:
                    del nums[j]
                    length = len(nums)
                else:
                    break
            i += 1
                    
