# https://leetcode.com/problems/container-with-most-water/

# Container With Most Water
'''
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by
array [1,8,6,2,5,4,8,3,7]
In this case, the max area of water (blue section)
the container can contain is 49.
'''
from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        '''
        # Brute Force: O(n^2) time
        #(For large input, time exceeded error)
        res = 0
        for left in range(len(height)):
            for right in range(len(height)):
                # area of rectangle = length * height
                area = (right - left) * min(height[left], height[right])
                res = max(area, res)     
        return res
        '''
        
        # Optimal Solution
        res = 0
        left = 0
        right = len(height) - 1
        while left < right:
            #calculate area
            area = (right - left) * min(height[left], height[right])
            res = max(res, area)
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            '''
            if height[left] > height[right], then
                right -=1
            if height[left] == height[right], then 
            we can left+=1 OR we can also right-=1
            '''
            
        #finally return the result        
        return res

height = [1,8,6,2,5,4,8,3,7]
print(Solution().maxArea(height))
