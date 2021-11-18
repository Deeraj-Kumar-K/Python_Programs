# https://leetcode.com/problems/intersection-of-two-arrays-ii/

# Intersection of Two Arrays II
# Given two integer arrays, return an array of their intersection
# Each element must appear as many times as it shows in both arrays
# and you may return the result in any order.
'''
Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.
'''

from collections import Counter
def intersect(nums1, nums2):
    # Counter={value1:counts, val2:counts, ...etc}
    hashTable = Counter(nums1)
    result = []
    for value in nums2:
       if value in hashTable and hashTable[value]!=0:
          hashTable[value] -= 1
          result.append(value)
    return result


nums1 = [1,2,2,1]
nums2 = [2,2]
print(intersect(nums1, nums2))
