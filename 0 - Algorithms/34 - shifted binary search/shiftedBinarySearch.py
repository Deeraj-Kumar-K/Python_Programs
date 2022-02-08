# Shifted Binary Search

# Given a sorted array of integers and a target integer. But there is a change.
# The numbers in the array have been shifted by some amount.
# Meaning, they have been moved to the left or the right by one or more positions.
# For example, [1, 2, 3, 4, 5] might become [3, 4, 5, 1, 2].
# Use a variation of Binary Search algorithm to find if the target number is present
# in the array and return its index value. If it is not present then, return -1.
'''
Explanation:

array = [75, 76, 77, 0, 1, 21, 33, 45, 45, 62]
target = 77, Output : 2

We have sorted elements [0, 1, 21, 33, 45, 45, 62, 75, 76, 77]
But they are shifted and we got [75, 76, 77, 0, 1, 21, 33, 45, 45, 62]
So we have to use a variation of binary search to find the element in this array.
'''

# Solution 1 : Using Recursion
# Time complexity: O(log(n)) , Space complexity: O(log(n))
#where n is the no. of elements in the array
'''
def shiftedBinarySearch(array, target):
    return shiftedBinarySearchHelper(array, target, 0, len(array) - 1)

def shiftedBinarySearchHelper(array, target, left, right):
    #base case
    if left > right: #element not found
        return -1

    mid = (left + right) // 2
    potentialMatch = array[mid]
    leftNum = array[left]
    rightNum = array[right]
    if potentialMatch == target:
        return mid
    elif leftNum <= potentialMatch: #if elements are sorted from 'left' to 'mid' 
        if target >= leftNum and target < potentialMatch:
            return shiftedBinarySearchHelper(array, target, left, mid - 1)
        else:
            return shiftedBinarySearchHelper(array, target, mid + 1, right)
    else: #else if elements are sorted from 'mid' to 'right'
        if target > potentialMatch and target <= rightNum:
            return shiftedBinarySearchHelper(array, target, mid + 1, right)
        else:
            return shiftedBinarySearchHelper(array, target, left, mid - 1)
'''

# Solution 2 : Using Iteration
# Time complexity: O(log(n)) , Space complexity: O(1)

def shiftedBinarySearch(array, target):
    return shiftedBinarySearchHelper(array, target, 0, len(array) - 1)

def shiftedBinarySearchHelper(array, target, left, right):
    while left <= right:
        mid = (left + right) // 2
        midNum = array[mid]
        leftNum = array[left]
        rightNum = array[right]
        if midNum == target:
            return mid
        elif leftNum <= midNum:
            if target >= leftNum and target < midNum:
                right = mid - 1 #search on left part of array
            else:
                left = mid + 1 #search on right part of array
        else:
            if target > midNum and target <= rightNum:
                left = mid + 1 #search on right part of array
            else:
                right = mid - 1 #search on left part of array
    #if loop breaks, element not found
    return -1


# Input
array = [75, 76, 77, 0, 1, 21, 33, 45, 45, 62]
target = 77
print(shiftedBinarySearch(array, target))
#output: 2
