# https://leetcode.com/problems/merge-sorted-array/

# Merge Sorted Array
# Given two integer arrays, sorted in non-decreasing order
# integers m and n, representing no. of elements in nums1 and nums2
# Merge nums1 and nums2 into a single array sorted in non-decreasing order
# Final sorted array should be stored inside the array nums1
'''
Example 1:
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

Example 2:
Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].

Constraints:
nums1.length == m + n
nums2.length == n
'''

def merge(nums1, nums2, m, n):
    lenA = m + n
    lenB = n
    # nums1.length == m + n
    # nums2.length == n
    i = lenA - lenB
    j = 0
    while i<lenA and j<lenB:
        if nums1[i] == 0:
            nums1[i]=nums2[j]
            j += 1
        i += 1
    nums1.sort()
    print(nums1)


nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
#Calling merge functiom
merge(nums1, nums2, m, n)
