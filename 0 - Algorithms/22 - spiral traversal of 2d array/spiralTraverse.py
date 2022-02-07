# Spiral Traverse

#Given 2-D array of integers, having square or rectangular shape
#Return 1-D array of all elements traversed in spiral order.
#Spiral order is we go from left->right, top->down, right->left, bottom->top.

'''
Example:

Given 2D array:
    sC       eC
sR   1  2  3 4
    12 13 14 5
    11 16 15 6
eR  10  9  8 7

where, sR-startRow, eR-endRow, sC-startCol, eC-endCol

Output: [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
The given array is traversed in spiral order.
'''

# Solution 1 : Using Iteration
# O(n) time , O(n) space , where n is no. of elements in array
#we store n elements in result array, so O(n) space, otherwise O(1) space
'''
def spiralTraverse(array):
    res = []
    startRow, endRow = 0, len(array) - 1
    startCol, endCol = 0, len(array[0]) - 1

    while startRow <= endRow and startCol <= endCol:
        #left to right direction
        for col in range(startCol, endCol + 1):
            res.append(array[startRow][col])

        #top to down
        for row in range(startRow + 1, endRow + 1):
            res.append(array[row][endCol])

        #right to left
        for col in reversed(range(startCol, endCol)): #endCol is not included
            res.append(array[endRow][col])

        #bottom to up
        for row in reversed(range(startRow + 1, endRow)): #endRow is not included
            res.append(array[row][startCol])

        startRow += 1
        endRow -= 1
        startCol += 1
        endCol -= 1
        
    return res
'''
'''
# Solution 2 : Using Recursion
# O(n) time , O(n) space , where n is no. of elements in array

def spiralTraverse(array):
    res = []
    spiralHelper(array, 0, len(array)-1, 0, len(array[0])-1, res)
    return res

def spiralHelper(array, startRow, endRow, startCol, endCol, res):
    if startRow > endRow or startCol > endCol:
        return
    
    for col in range(startCol, endCol + 1):
        res.append(array[startRow][col])

    for row in range(startRow + 1, endRow + 1):
        res.append(array[row][endCol])

    for col in reversed(range(startCol, endCol)):
        res.append(array[endRow][col])

    for row in reversed(range(startRow + 1, endRow)):
        res.append(array[row][startCol])

    spiralHelper(array, startRow+1, endRow-1, startCol+1, endCol-1, res) 
    
array = [[1,2,3],[8,9,4],[7,6,5]]
for row in array:
    print(row)
print("\nSpiral Traverse: \n",spiralTraverse(array))
'''

# *****************************NEW UPDATE********************************

'''
The above solution gives wrong answer for inputs like:

Input - 1 :
[
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12]
    ]

Input - 2 : Array with only one column.
 [
    [1],
    [2],
    [3]
 ]

Input - 3: Array with only one row.
 [
     [1,2,3]
 ]

 So, an updated solution which works is given below.
'''

class Solution:
    def spiralOrder(self, array):
        
        # Solution 1 : Using Iteration
        # O(m * n) time , O(1) space
        #where m and n are the no. of rows and columns
        '''
        res = []
        startRow, endRow = 0, len(array) - 1
        startCol, endCol = 0, len(array[0]) - 1

        while startRow <= endRow and startCol <= endCol:
            #left to right direction
            for col in range(startCol, endCol + 1): #endCol + 1 is excluded
                res.append(array[startRow][col])
            startRow += 1

            #top to down
            for row in range(startRow, endRow + 1): #endRow + 1 is excluded
                res.append(array[row][endCol])
            endCol -= 1
            
            #this condition is for the 1-D arrays like Ex: [[7], [8], [9]] - this array has single column only
            if not (startRow <= endRow and startCol <= endCol): #so we need to break our loop
                break #otherwise we will get wrong answer
                
            #right to left
            for col in reversed(range(startCol, endCol + 1)): #endCol + 1 is not included
                res.append(array[endRow][col])
            endRow -= 1

            #bottom to up
            for row in reversed(range(startRow, endRow + 1)): #endRow + 1 is not included
                res.append(array[row][startCol])
            startCol += 1

        return res
        '''
    
        # Solution 2 : Using Recursion
        # O(n) time , O(n) space , where n is no. of elements in array
        
        def spiralHelper(array, startRow, endRow, startCol, endCol, res):
            #Base case for recursion
            if startRow > endRow or startCol > endCol:
                return

            #left to right direction
            for col in range(startCol, endCol + 1):
                res.append(array[startRow][col])
            startRow += 1 #first row is traversed completely, so increment startRow

            #top to down
            for row in range(startRow, endRow + 1):
                res.append(array[row][endCol])
            endCol -= 1 #last column is traversed completely, so decrement endCol
            
            #edge case: 1-D array having single row or single column only
            # if not (startRow <= endRow and startCol <= endCol): 
            #     return
            if startRow > endRow or startCol > endCol:
                return
                
            #right to left
            for col in reversed(range(startCol, endCol + 1)):
                res.append(array[endRow][col])
            endRow -= 1 #last row is traversed completely, so decrement endRow

            #bottom to up
            for row in reversed(range(startRow, endRow + 1)):
                res.append(array[row][startCol])
            startCol += 1 #first column is traversed completely, so increment startCol
            
            spiralHelper(array, startRow, endRow, startCol, endCol, res)
            
        res = []
        spiralHelper(array, 0, len(array)-1, 0, len(array[0])-1, res)
        return res

# Input
array = [
    [1],
    [2],
    [3]
 ]
print(Solution().spiralOrder(array))
#output : [1,2,3]
