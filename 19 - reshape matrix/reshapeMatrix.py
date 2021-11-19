# https://leetcode.com/problems/reshape-the-matrix/

# Reshape the Matrix
'''
Example 1:
Input: mat = [[1,2],[3,4]], r = 1, c = 4
Output: [[1,2,3,4]]

Example 2:
Input: mat = [[1,2],[3,4]], r = 2, c = 4
Output: [[1,2],[3,4]]
'''

class Solution:
    
    # calculate no.of elements inside matrix
    def countElements(self,arr): 
        count = 0
        for element in arr:
            if type(element) is list:
                count += self.countElements(element)
                continue
            count += 1
        return count
    
    # create 1-d array of matrix
    def joinArr(self,arr): 
        a = []
        for element in arr:
            if type(element) is list:
                a.extend(self.joinArr(element))
                continue
            a.append(element)
        return a
     
    # function to reshape the matrix
    def matrixReshape(self, mat, r, c):
        counts = self.countElements(mat) # no. of elements inside matrix
        if r*c == counts:
            arr = []
            result = []
            temp=[]
            counter=0
            arr.extend(self.joinArr(mat))
            for row in range(r):
                for col in range(c):
                    temp.append(arr[counter])
                    counter += 1
                result.append(temp)
                temp=[]
            return result
        else:
            return mat


mat = [[1,2],[3,4]]
r = 2
c = 4
print(Solution().matrixReshape(mat,r,c))
