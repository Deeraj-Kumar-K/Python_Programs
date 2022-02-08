# Search in Sorted Matrix

# Given a 2-D array (matrix) of distinct integers where each row is sorted and
# each column is also sorted. Given a target number, you must find the number
# and return an array of [row, col] index values of the target number.
# Return [-1, -1] if target number is not present in the matrix

'''
Explanation:

All the rows and columns of the matrix are sorted in ascending order.

    [1, 4, 7, 12, 15, 900],
    [2, 5, 19, 31, 32, 901],
    [3, 8, 24, 33, 35, 902],
    [50, 51, 52, 54, 55, 903],
    [90, 92, 94, 98, 99, 904],

target value = 54

We start our search from the last column of the first row.
We see that '900' > target, so move our pointer to the left column.
Now pointer points to '15' and '15' < '54', so move to the row below.
We don't go to the left column coz all numbers to the left are even smaller than '15'.
So we move our pointer to the row below coz even the columns are in sorted order.
Now, we have '32' < '54' so move to the row below. We get '35' < '54', so go down.
We get '55' and '55' > '54' so we move to the left column.
Finally we have a match i.e '55' == '55' and so return the indices.
Output : [3 , 3]
'''

# Time complexity: O(n + m) , Space complexity: O(1)
#where n is the no. of rows and m is the no. of columns in the matrix

def searchInSortedMatrix(matrix, target):
    row = 0 #we start from first row
    col = len(matrix[0]) - 1 #and last column of the matrix
    #while we remain inside the bounds of the array, loop executes
    while row < len(matrix) and col >= 0:
        if matrix[row][col] > target: #if currentNum > target then,
            col -= 1 #go to the left column since elements are sorted
        elif matrix[row][col] < target: #if currentNum < target then,
            row += 1 #go to the below row since columns are also sorted
        else: #else if currentNum == target,
            return [row, col] #return indices value
    return [-1, -1] #if we are out of the loop, lement not found


# Input
matrix = [
    [1, 4, 7, 12, 15, 900],
    [2, 5, 19, 31, 32, 901],
    [3, 8, 24, 33, 35, 902],
    [50, 51, 52, 54, 55, 903],
    [90, 92, 94, 98, 99, 904],
]
target = 54
print(searchInSortedMatrix(matrix, target))
#output: [3, 3]
