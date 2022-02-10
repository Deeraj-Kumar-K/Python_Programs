# Quick Select

# Given an array of distinct integers and an integer k.
# Return the kth smallest number in that array in linear time, on average.
# The array may or may not be sorted.
'''
Explanation:

array = [20,30,50,10,40], k = 3

If we sort the array, we get [10, 20, 30, 40, 50]
1st smallest element is '10' in index '0'
2nd smallest number is '20' in index '1'
Similarly kth smallest element is in index 'k - 1'

In above example k = 3, so kth element is in index '2'
Output: 30

We find the k-th element by using quick sort variation i.e quick select.
Whenever our pivot is placed in its final sorted position,
we check if its the k-th position. If it is then return pivot value.
If not then explore one of the two subarrays where the k-th element will be present.

# Time and Space Complexity:

# Best case: when array is divided in half (pivot gets placed in middle)
# In 1st pass we have an array of length n, so O(n) operations for pivot
# then array divided into two half, we skip one half and continue on other,(1/2)*n,
# then that half again divided into half (1/4)*n operations and so on.
# This series gives [n + (1/2)n + (1/4)n + (1/8)n.... = n]. So O(n) time.

# Avg case: pivot gets placed in somewhere quarter of the array

# Worst case: every iteration, array is divided into 'n-1' and '1' element
# so 'n' operations are performed almost 'n' times. So total O(n^2) time.

# O(1) space coz we do it in-place using iteration.
# we don't use recursion coz we skip one of the two subarrays.
'''

# Best: O(n) time , O(1) space
# Average: O(n) time , O(1) space
# Worst: O(n^2) time, O(1) space

def quickSelect(array, k):
    position = k - 1 #kth element is present in (k-1) index position
    return quickSelectHelper(array, 0, len(array) - 1, position)

def quickSelectHelper(array, startIdx, endIdx, position):

    while True:
        if startIdx > endIdx: #it means we missed kth element, something is wrong
            raise Exception("Your Algorithm should not have reached here")
            #return "Your Algorithm should not have reached here"

        #everything below is same as quicksort until,
        pivotIdx = startIdx
        leftIdx = startIdx + 1
        rightIdx = endIdx
        while leftIdx <= rightIdx:
            if array[leftIdx] > array[pivotIdx] and array[rightIdx] < array[pivotIdx]:
                swap(leftIdx, rightIdx, array)
            if array[leftIdx] <= array[pivotIdx]:
                leftIdx += 1
            if array[rightIdx] >= array[pivotIdx]:
                rightIdx -= 1
                
        swap(pivotIdx, rightIdx, array)

        # until here
        #now when pivot is in its final sorted place, we check if its in kth position 
        if rightIdx == position: #if it is in kth position then,
            return array[rightIdx] #return the pivot
        elif rightIdx < position: #else if our pivot position < kth position,
            startIdx = rightIdx + 1 #then explore on right side, skip left subarray
        else:
            endIdx = rightIdx - 1 #else explore left subarray, skip right subarray
    #now next iteration happens using our updated pointers until kth element is found

def swap(a, b, array):
    array[a], array[b] = array[b], array[a]


# Input
array = [20,30,50,10,40]
k = 3
result = quickSelect(array, k)
print("Kth smallest element:",result)
#output = 30
