# Heap Sort

# Given an array of integers, return a sorted version of that array.
# Use Heap Sort algorithm to sort the array.
'''
Explanation:

We first build MAX Heap of the given unsorted array.
Then we swap 1st element with last element, so now last element is sorted.
Now the root element needs to be sifted Down to its correct place.
After siftDown, again we have the max value on top/1st element.
Now again perform the same steps until array is sorted.

Swap the 1st number in array with last 2nd index.
Perform siftDown. Then swap 1st element with last 3rd index, etc.
Finally we will have only one elemnt remaining in the heap and
so it is in its sorted place. Looping stops and our array is sorted.


# Time and Space Complexity:

# Building the max heap takes O(n) time, and
# we perform siftDown operation which takes O(log(n)) time, for 'n' elements,
# so overall time complexity is O(nlog(n)) time.

# O(1) space because we don't use extra memory and do everything in-place.
'''

# Best: O(nlog(n)) time , O(1) space
# Average: O(nlog(n)) time , O(1) space
# Worst: O(nlog(n)) time , O(1) space
# where n is the no. of elements in the input array

def heapSort(array):
    buildHeap(array) # build max heap
    # we loop from end of array to idx '1' because when we have only one
    # element remaining in array ie. idx '0', it is already sorted
    for endIdx in reversed(range(1, len(array))):
        swap(0, endIdx, array) # swap 1st element with last element in array
        siftDown(0, endIdx - 1, array) # then siftDown 1st element until endIdx - 1
    return array

def swap(a, b, array):
    array[a], array[b] = array[b], array[a]

# O(n) time , O(1) space
def buildHeap(array):
    firstParentIdx = (len(array) - 2) // 2
    for currentIdx in reversed(range(firstParentIdx + 1)):
        siftDown(currentIdx, len(array) - 1, array)

# O(log(n)) time , O(1) space
def siftDown(currentIdx, endIdx, heap):
    childOneIdx = 2 * currentIdx + 1
    while childOneIdx <= endIdx:
        childTwoIdx = 2 * currentIdx + 2 if 2*currentIdx+2 <= endIdx else -1
        if childTwoIdx > -1 and heap[childTwoIdx] > heap[childOneIdx]:
            idxToSwap = childTwoIdx
        else:
            idxToSwap = childOneIdx
        if heap[idxToSwap] > heap[currentIdx]:
            swap(currentIdx, idxToSwap, heap)
            currentIdx = idxToSwap
            childOneIdx = 2 * currentIdx + 1
        else:
            return


# Input
array = [2,3,5,1,4,6]
print("Before Sorting:", array)
print("After Sorting:", heapSort(array))
#output = [1,2,3,4,5,6]
