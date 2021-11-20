# https://leetcode.com/problems/first-bad-version/

# First Bad Version
# While developing a new product, it fails quality check.
# Since each version is developed based on the previous version,
# all the versions after a bad version are also bad.
# Find out the first bad one, which causes all the following ones to be bad.
'''
Example 1:
Input: n = 5, bad = 4
Output: 4

Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.
'''

# The isBadVersion API is already defined for you.
class Solution:
    def firstBadVersion(self, n):      
        left = 0
        right = n
        middle = 0
        #to minimize the number of calls to the API, binary search
        while left <= right:
            middle = (left + right) // 2
            
            if isBadVersion(middle) == False:
                left = middle + 1
            else:
                if isBadVersion(middle - 1 ) == False:
                    return middle
                else:
                    right = middle - 1
        return middle
