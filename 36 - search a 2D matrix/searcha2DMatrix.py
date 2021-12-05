# https://leetcode.com/problems/search-a-2d-matrix/

# Search a 2D Matrix
#This matrix has the following properties:
#Integers in each row are sorted from left to right.
#First integer of each row is > last integer of the previous row.
'''
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
Output: true

target = 13
Output: false
'''

from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix)-1
        #applying binary search for finding row
        while left < right:
            mid = (left + right) // 2
            if matrix[mid][0] == target:
                return True
            if matrix[mid][len(matrix[0])-1] == target:
                return True
            elif target < matrix[mid][0]:
                right = mid - 1
            elif target > matrix[mid][len(matrix[0])-1]:
                left = mid + 1
            else:
                break
            #if target value is not present in the previous row or next row,
            #it should be present in the current row (i.e mid), so break the loop
            
        #if target doesnt exist, return false
        if left > right:
            return False
        
        #applying binary search for finding target value
        if left == right: #if both pointer are overlapping, select anyone
            row = left
        else:
            row = mid #target is probably present in the current row(i.e mid)
        left = 0
        right = len(matrix[0])-1
        while left <= right:
            mid = (left + right) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return False

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
print(Solution().searchMatrix(matrix, target))
print()
target = 13
print(Solution().searchMatrix(matrix, target))
