# https://leetcode.com/problems/pascals-triangle/

# Pascal's Triangle
'''
In Pascal's triangle, each number is the sum of the two numbers
directly above it as shown:
    1
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1

Example 1:
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Example 2:
Input: numRows = 1
Output: [[1]]
'''

from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        arr = []
        temp = []
        counter=1
        for row in range(numRows):
            for col in range(counter):
                if col==0 or col==counter-1:
                    temp.append(1)
                else:
                    temp.append(arr[row-1][col-1]+arr[row-1][col])
            arr.append(temp)
            temp=[]
            counter+=1
        return arr

print(Solution().generate(5))
