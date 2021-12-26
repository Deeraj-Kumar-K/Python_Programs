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
'''   
    
array = [[1,2,3],[8,9,4],[7,6,5]]
for row in array:
    print(row)
print("\nSpiral Traverse: \n",spiralTraverse(array))
