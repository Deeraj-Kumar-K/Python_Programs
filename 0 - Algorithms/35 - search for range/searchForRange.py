# Search for Range (using Binary Search variation)

# Given a sorted array of integers and a target integer.
# Use a variation of the Binary Search algorithm to find a range of indices
# in between which the target number is contained in the array.
# [startIdx, endIdx] where "startIdx" represents first index at which
# the target number is located while "endIdx" represents the last index
# at which the target number is located. Return [-1, -1] if the number is not present.
'''
Explanation:

Input: [0, 1, 20, 33, 45, 45, 45, 45, 45, 45, 63, 72, 75], target = 45
Output: [4, 9]

Our target number '45' starts at index '4' and ends at index '9'.
So we return the output array as [4, 9].
'''

# Solution 1 : Using Recursion
# Time complexity: O(log(n)) , Space complexity: O(log(n))
#where n is the no. of elements in input array
'''
def searchForRange(array, target): # total O(2 * log(n)) time = O(log(n)) time
    finalRange = [-1, -1]
    binarySearchVariation(array, target, 0, len(array)-1, finalRange, True) #O(log(n)) time
    binarySearchVariation(array, target, 0, len(array)-1, finalRange, False) #O(log(n)) time
    return finalRange

def binarySearchVariation(array, target, left, right, finalRange, goLeft):
    #base condition
    if left > right:
        return

    mid = (left + right) // 2
    if array[mid] < target:
        binarySearchVariation(array, target, mid + 1, right, finalRange, goLeft)
    elif array[mid] > target:
        binarySearchVariation(array, target, left, mid - 1, finalRange, goLeft)
    else:
        if goLeft:
            if mid == 0 or array[mid - 1] != target:
                finalRange[0] = mid
            else:
                binarySearchVariation(array, target, left, mid - 1, finalRange, goLeft)
        else:
            if mid == len(array) - 1 or array[mid + 1] != target:
                finalRange[1] = mid
            else:
                binarySearchVariation(array, target, mid + 1, right, finalRange, goLeft)
    '''

# Solution 2 : Using Iteration
# Time complexity: O(log(n)) , Space complexity: O(1)
#where n is the length of input array

def searchForRange(array, target):
    finalRange = [-1, -1]
    binarySearchVariation(array, target, 0, len(array)-1, finalRange, True) #to find startIdx
    binarySearchVariation(array, target, 0, len(array)-1, finalRange, False) #to find endIdx
    return finalRange

def binarySearchVariation(array, target, left, right, finalRange, goLeft):
    while left <= right:
        mid = (left + right) // 2
        if array[mid] < target:
            left = mid + 1
        elif array[mid] > target:
            right = mid - 1
        else: #if array[mid] == target, so we have found out target value
            if goLeft: #if goLeft is true, we will search on left side to find 'startIdx'
                # mid == 0 means we have reached the extreme left of array so range starts from here
                # or if "mid - 1" value i.e previous number != target then also range starts from here
                if mid == 0 or array[mid - 1] != target:
                    finalRange[0] = mid
                    return #we return coz we have found the 'startIdx' so no need to continue further
                else: #if 'startIdx' not found, continue searching on left side of array
                    right = mid - 1
            else: #if goLeft is false, then search on right side of array to find 'endIdx'
                # if we have reached the end of array or if the next number "mid + 1" != target number,
                # then we have found the end of the range
                if mid == len(array) - 1 or array[mid + 1] != target:
                    finalRange[1] = mid
                    return
                else: #else continue to search on right side to find 'endIdx'
                    left = mid + 1
                
                
# Input
array = [5, 7, 7, 9, 9, 10]
target = 7
print(searchForRange(array, target))
#output: [1, 2]
array = [0, 1, 20, 33, 45, 45, 45, 45, 45, 45, 63, 72, 75]
target = 45
print(searchForRange(array, target))
#output: [4, 9]
