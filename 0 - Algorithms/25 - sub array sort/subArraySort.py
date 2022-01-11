# Sub-Array Sort

# Given an array of length atleast two, find the smallest sub-array within the input array,
# such that when it is sorted, it makes the entire input array sorted.
# Return the starting and ending index value of that smallest sub-array.
'''
Solution:
First, we need to find the smallest and largest number that is unsorted.
Then we need to find the final sorted position of those two number in the array.
Those index values of their final position will be the final result.

##############################################################
Example 1:
Input: [5,6,7,8,9,-1]
Smallest Unsorted Number = -1, Largest Unsorted Number = 9
Final sorted position of '-1' is in the beginning of the array i.e. index '0' and
final sorted position of '9' is in the end of the array i.e. index '5'

So, smallest sub-array that needs to be sorted in-order to make entire input array sorted
will be the entire array itself.
Output: [0, 5]

##############################################################
Example 2:
Input: [1,3,5,7,10,11,7,12,6,7,18,19,20]

Smallest sub-array that needs sorting is [7,10,11,7,12,6,7]

Smallest Unsorted Number = 6, Largest Unsorted Number = 12
Final sorted position of '6' is after'5' i.e. index '3' and
final sorted position of '12' is before '18' i.e. index '9'

Output: [3, 9]
'''

# Solution : O(n) time , O(1) space

def subArraySort(array):
    minOutOfOrderNum = float('inf')
    maxOutOfOrderNum = float('-inf')
    
    for i in range(len(array)):
        num = array[i]
        #helper function checks if current number is unsorted 
        if isOutOfOrder(num, i , array): #if it is true, update min and max values
            minOutOfOrderNum = min(minOutOfOrderNum, num)
            maxOutOfOrderNum = max(maxOutOfOrderNum, num)

    #edge case, if input array is already sorted        
    if minOutOfOrderNum == float('inf'): #we can also check maxOutOfOrderNum
        return [-1, -1]

    #now lets find the final position of minOutOfOrderNum and maxOutOfOrderNum
    leftIdx = 0
    while minOutOfOrderNum >= array[leftIdx]:
        leftIdx += 1

    rightIdx = len(array)-1
    while maxOutOfOrderNum <= array[rightIdx]:
        rightIdx -= 1
        
    return [leftIdx, rightIdx]

#helper function to check if number is unsorted/out of order
def isOutOfOrder(num, i, array):
    #if num is 1st number in the array
    if i == 0:
        return num > array[i + 1]

    #if num is last number in the array
    if i == len(array)-1:
        return num < array[i - 1]

    #if num is any number in the middle of the array
    return num > array[i + 1] or num < array[i - 1]



array = [5,6,7,8,9,-1]
print(array)
print(subArraySort(array))
print()
array = [1,2,4,7,10,11,7,12,6,7,16,18,19]
print(array)
print(subArraySort(array))
