# Merge Sort

# Given an array of integers, return a sorted version of that array.
# Use Merge Sort algorithm to sort the array.
'''
Explanation:

Merge sort is a divide and conquer algorithm.

We can implement mergeSort by using two approaches:

1. By recursively creating new arrays for dividing and merging subarrays

# It takes O(nlog(n) time
Because recursively dividing array into halves will create log(n) levels,
and every level takes O(n) operations
# It takes O(nlog(n)) space
Because overall we use O(nlog(n)) space while implementing mergeSort.

2. By creating a copy of mainArray and sorting mainArray in-place

# It takes O(nlog(n) time
Same as above because recursively dividing array into halves create log(n) levels,
and every level takes O(n) operations
# It takes O(n) space
Because we just create one copy of mainArray which takes O(n) space.
'''

'''
# Solution 1 : By creating new arrays

# Best: O(nlog(n)) time , O(nlog(n)) space
# Average: O(nlog(n)) time , O(nlog(n)) space
# Worst: O(nlog(n)) time , O(nlog(n)) space
# where n is the no. of elements in the input array

def mergeSort(array):
    # base case, if one element in array, it is sorted
    if len(array) == 1:
        return array

    middle = len(array) // 2
    leftHalf = array[ : middle] # here, middle is excluded
    rightHalf = array[middle : ] # here, middle is included in slicing
    # we can also include middle in leftHalf and exlude in rightHalf
    return mergeSortedArrays(mergeSort(leftHalf), mergeSort(rightHalf))

def mergeSortedArrays(leftHalf, rightHalf):
    # creating new array which will be sorted
    sortedArray = [None] * (len(leftHalf) + len(rightHalf)) # initializing with 'None'
    k = 0 # points to index of sortedArray
    i, j = 0, 0
    while i < len(leftHalf) and j < len(rightHalf):
        if leftHalf[i] <= rightHalf[j]:
            sortedArray[k] = leftHalf[i]
            i += 1
        else:
            sortedArray[k] = rightHalf[j]
            j += 1
        k += 1
    while i < len(leftHalf):
        sortedArray[k] = leftHalf[i]
        i += 1
        k += 1
    while j < len(rightHalf):
        sortedArray[k] = rightHalf[j]
        j += 1
        k += 1
    return sortedArray
'''    

# Solution 2 : Creating one auxiliary array and modifying input array in-place

# Best: O(nlog(n)) time , O(n) space
# Average: O(nlog(n)) time , O(n) space
# Worst: O(nlog(n)) time , O(n) space
# where n is the no. of elements in the input array

def mergeSort(array):
    # base case, if one element or empty array
    if len(array) <= 1:
        return array

    auxiliaryArray = array[ : ] # creating a copy of mainArray
    mergeSortHelper(array, 0, len(array) - 1, auxiliaryArray)
    return array

def mergeSortHelper(mainArray, startIdx, endIdx, auxiliaryArray):
    #base case, if one element in array
    if startIdx == endIdx:
        return #not returning anything coz we are not creating new arrays

    middleIdx = (startIdx + endIdx) // 2
    # we call helper method and pass mainArray as auxiliaryArray and vice versa
    mergeSortHelper(auxiliaryArray, startIdx, middleIdx, mainArray) # leftHalf
    mergeSortHelper(auxiliaryArray, middleIdx + 1, endIdx, mainArray) # rightHalf
    doMerge(mainArray, startIdx, middleIdx, endIdx, auxiliaryArray) # then merge them

def doMerge(mainArray, startIdx, middleIdx, endIdx, auxiliaryArray):
    k = startIdx # points to sortedArray i.e mainArray
    i = startIdx # points to 1st subarray in auxiliaryArray
    j = middleIdx + 1 # points to 2nd subarray in auxiliaryArray
    while i <= middleIdx and j <= endIdx:
        if auxiliaryArray[i] <= auxiliaryArray[j]:
            mainArray[k] = auxiliaryArray[i]
            i += 1
        else:
            mainArray[k] = auxiliaryArray[j]
            j += 1
        k += 1
    while i <= middleIdx:
        mainArray[k] = auxiliaryArray[i]
        i += 1
        k += 1
    while j <= endIdx:
        mainArray[k] = auxiliaryArray[j]
        j += 1
        k += 1
    # here, we don't return anything, coz sorting is done in-place
            
    
# Input
array = [2,3,5,1,4,6]
print("Before Sorting:", array)
print("After Sorting:", mergeSort(array))
# Output = [1,2,3,4,5,6]
