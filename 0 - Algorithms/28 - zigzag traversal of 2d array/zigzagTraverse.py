# ZigZag Traverse

#Given 2-D array of integers, having square or rectangular shape
#Return 1-D array of all elements traversed in zigzag order.
#ZigZag order is explained below with example.

'''
Example:
Input: [[1,3,4,10],[2,5,9,11],[6,8,12,15],[7,13,14,16]]
         
Given 2D array:

    1   3   4  10
    2   5   9  11
    6   8  12  15
    7  13  14  16

First we go down ie. 1->2, then we go diagonally up to the right, ie. 2->3,
until we reach first row or last column. Once we reach there,
we change the direction to go diagonally downwards to the left,
and we move to the right if we are in 1st row. If we are in last column, move down.

Now our direction of traversal is diagonally downwards to the left,
so we go until we reach last row or 1st column. Once we reach there,
we change the direction to go diagonally upwards to the right,
and if we have currently reached the 1st row, move to right.
Or if we are in last column, move down.

Same steps are repeated until we go out of bounds of the input array.

Output: [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
The given array is traversed in zigzag order.
'''

# Solution : O(n) time , O(n) space
#where n is no. of elements in the 2-D array
#we store n elements in result array, so O(n) space, otherwise O(1) space

def zigzagTraverse(array):
    height = len(array) - 1
    width = len(array[0]) - 1
    result = []
    goingDown = True #keeps track of direction of traversal
    row = 0
    col = 0
    #while we are not out of bounds of array,
    while not isOutOfBounds(row, col, height, width):
        result.append(array[row][col])
        #if we are traversing in downwards direction and,
        if goingDown: 
            if col == 0 or row == height: #if we reach 1st column or last row then
                goingDown = False #change the direction to goingUp
                if row == height: #if we reach last row then
                    col += 1 #move to right
                else: #else we reach to 1st column
                    row += 1 #then move down
            else: #if we have not reached 1st column or last row then,
                row += 1 #move diagonally down,
                col -= 1 #to the left direction
                
        #else if we are traversing in upwards direction and,
        else:
            if row == 0 or col == width: #if we reach 1st row or last column then
                goingDown = True #change the direction to goingDown
                if col == width: #if we reach last column then
                    row += 1 #move down
                else: #else we have reached to 1st row
                    col += 1 #move to right
            else: #if we have not reached 1st row or last column then,
                row -= 1 #move diagonally up,
                col += 1 #to the right direction
    #finally return the 1-D result array
    return result

#helper function to check if we are out of bounds of the array
def isOutOfBounds(row, col, height, width):
    #return true if we go out of bounds of array i.e -ve values or ahead of its length
    return row < 0 or col < 0 or row > height or col > width
   
    
array = [[1,3,4,10],
         [2,5,9,11],
         [6,8,12,15],
         [7,13,14,16]]
#displaying the input array
for row in array:
    print(row)
#displaying the result after zigzag traverse
print("\nZigZag Traverse: \n", zigzagTraverse(array))
