# Quick Sort (in-place Recursive solution)
'''
Explanation:

Ex: [20,30,50,10,40] - unsorted input array
The first element always chosen as pivot. Pivot=20
2nd element is pointed by 'left' pointer. LeftNum=30
Last element is pointed by 'right' pointer. RightNum=40

When Pivot will get placed in its sorted position,
Pivot element will divide the array into two subarrays.
So every number to the left of pivot will be less than pivot and
every number to the right of pivot will be greater than pivot.

Left pointer gets increments until "leftNum <= pivot".
If leftNum is smaller or equal, it means they are in their correct place.

Similarly, Right pointer gets decremented until "rightNum >= pivot".
If rightNum is greater or equal, it means they are in their correct place.

When we get a leftNum > pivot and rightNum < pivot, we swap them.

Finally when the loop breaks, it means leftIdx > rightIdx.
So now leftNum will be greater than rightNum.
Ex: [30, 10, 20, 40, 50]
here, pivot=30, leftIdx=3, leftNum=40, rightIdx=2, rightNum=20
Now, leftIdx > rightIdx and now leftNum > rightNum and rightNum <= pivot
Swap pivot element with rightIdx. Now pivot is in its final place.
We get [10, 20, 30, 40, 50] after swapping.

Pivot divides the array into two subarrays.
Check which subarray is smaller, and then recursively call quicksort
on smaller subarray first and then on the larger subarray.

# Time and Space Complexity

# Best case: when array is divided in half (pivot get placed in middle)
# 'n' no. of operations to place pivot in its correct position.
# since array keeps on dividing into two halves, O(log(n)) operations.
# So total n*logn time.

# Worst case: every iteration, array is divided into 'n-1' and '1' element
# so 'n' operations are performed almost 'n' times. So total O(n^2) time.

#O(log(n)) space coz we sort smaller subarray first and use tail recursion

# O(n) space when we sort 'n-1' subarray first. So 'n' frames on call stack.
'''

# Best: O(nlog(n)) time , O(log(n)) space
# Average: O(nlog(n)) time , O(log(n)) space
# Worst: O(n^2) time, O(n) space

def quickSort(array):
    quickSortHelper(array, 0, len(array)-1)
    return array

def quickSortHelper(array, startIdx, endIdx):
    #base case, if array has 0 or 1 element
    if startIdx >= endIdx:
        return

    #to choose a random pivot element
    #pivotIdx = getRandomBetween(startIdx, endIdx) #use random library
    #swap(pivotIdx, startIdx) #then swap random element with first element
    
    #first element is always chosen as pivot
    pivotIdx = startIdx
    pivot = array[startIdx]
    left = startIdx + 1
    right = endIdx
    while left <= right:
        if array[left] > pivot and array[right] < pivot:
            swap(left, right, array)
        if array[left] <= pivot:
            left += 1
        if array[right] >= pivot:
            right -= 1
            
    # now, 'right' points to smaller number than pivot so swap
    swap(pivotIdx, right, array) #now pivot is placed in its sorted position

    #check which subarray is smaller, subarray on left of pivot or on the right
    leftSubArrayIsSmaller = [right - 1 - startIdx] < [endIdx - (right + 1)]
    if leftSubArrayIsSmaller:
        quickSortHelper(array, startIdx, right - 1) #sort left subarray first
        quickSortHelper(array, right + 1, endIdx) #then right subarray
    else:
        quickSortHelper(array, right + 1, endIdx) #right subarray
        quickSortHelper(array, startIdx, right - 1) #left subarray

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]


array = [20,30,50,10,40]
print("Before sorting:",array)
result = quickSort(array)
print("\nAfter sorting:",result)
