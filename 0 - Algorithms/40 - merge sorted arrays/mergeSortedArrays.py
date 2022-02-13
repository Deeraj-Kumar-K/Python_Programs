# Merge Sorted Arrays

# Given 'k' sorted array, merge them into one single sorted array.
'''
Explanation:

Input :
[
    [1,5,8,21],
    [-1,0],
    [-125,81,121],
    [3,6,12,20,160]
]

Output: [-125, -1, 0, 1, 3, 5, 6, 8, 12, 20, 21, 81, 121, 160]
'''

# Solution 1 : By continuoulsy finding minimim number from 'k' arrays
# O(nk) time , O(n + k) space
# where 'n' is total no. of elements and 'k' is total no. of arrays
'''
def mergeSortedArrays(arrays):
    sortedList = []
    elementIdxs = [0 for array in arrays]
    while True:
        smallestItems = []
        for arrayIdx in range(len(arrays)):
            currentArray = arrays[arrayIdx]
            elementIdx = elementIdxs[arrayIdx]
            if elementIdx == len(currentArray):
                continue
            smallestItems.append({'arrayIdx': arrayIdx, 'num': currentArray[elementIdx]})
        if len(smallestItems) == 0:
            break
        minItem = getMinValue(smallestItems)
        sortedList.append(minItem['num'])
        elementIdxs[minItem['arrayIdx']] += 1     
    return sortedList

def getMinValue(items):
    minIdx = 0
    for i in range(1, len(items)):
        if items[i]['num'] < items[minIdx]['num']:
            minIdx = i
    return items[minIdx]
'''

# Solution 2 : Using Min Heap
# O(nlog(k) + k) time , O(n + k) space
# where 'n' is total no. of elements and 'k' is total no. of arrays

def mergeSortedArrays(arrays):
    sortedList = []
    smallestItems = []
    for arrayIdx in range(len(arrays)): # O(k)
        smallestItems.append({'arrayIdx': arrayIdx, 'elementIdx': 0, 'num': arrays[arrayIdx][0]})
    minHeap = MinHeap(smallestItems)
    while not minHeap.isEmpty(): # total O(n * (2*log(k) ) = O(nlog(k))
        minItem = minHeap.remove() # O(log(k))
        arrayIdx, elementIdx, num = minItem['arrayIdx'], minItem['elementIdx'],minItem['num']
        sortedList.append(num)
        if elementIdx == len(arrays[arrayIdx]) - 1:
            continue
        minHeap.insert({'arrayIdx': arrayIdx, 'elementIdx': elementIdx + 1, 'num': arrays[arrayIdx][elementIdx + 1]}) # O(log(k))
    return sortedList
        
    
class MinHeap:
    def __init__(self, array):
        self.heap = self.buildHeap(array) #building heap from input array

    # O(n) time , O(1) space
    def isEmpty(self):
        return len(self.heap) == 0

    # O(n) time , O(1) space
    def buildHeap(self, array):
        #we start from the parent of the last element in heap
        firstParentIdx = (len(array) - 2) // 2
        
        #all the nodes to the left of parent node are also parent nodes
        #Ex: [1,2,3,4,5] - len(arr) = 5 so last element's idx = 5 - 1 = 4
        #parentNode = i - 1 // 2, so we get (len(array) - 2)//2
        # firstParentIdx = (5 - 2)//2 = 1, so idx '1' = 2
        # '2' is the parent node of node '5' and all the nodes to its left
        #will also be parent node. Here, we have '1' on the left of '2'.

        #for loop from '0 to 5' in reversed is 4,3,2,1,0. '5' is excluded.
        for currentIdx in reversed(range(firstParentIdx + 1)):
            #we call siftDown for all parent nodes in tree from bottom to up
            self.siftDown(currentIdx, len(array) - 1, array)
        return array


    # O(1) time , O(1) space
    def peek(self):
        return self.heap[0] #root / min value

    def showHeap(self):
        return self.heap


    # O(log(n)) time , O(1) space
    def insert(self, value):
        self.heap.append(value) #new value is inserted at last position
        self.siftUp(len(self.heap)-1, self.heap) #then perform siftUp


    # O(log(n)) time , O(1) space
    def remove(self):
        #first swap root element with last element in heap
        self.swap(0, len(self.heap) - 1, self.heap)
        valueToRemove = self.heap.pop() #then pop the last element
        #now siftDown the new root element to its correct place in heap
        self.siftDown(0, len(self.heap) - 1, self.heap)
        return valueToRemove


    # O(log(n)) time , O(1) space
    def siftUp(self, currentIdx, heap):
        parentIdx = (currentIdx - 1) // 2
        
        #loop breaks if we reach the root node while performing siftUp
        #coz we can't siftUp the root element and loop also breaks if
        #currentNode's value > parent value, then no siftUp needed
        
        while currentIdx > 0 and heap[currentIdx]["num"] < heap[parentIdx]["num"]:
            self.swap(currentIdx, parentIdx, heap)
            currentIdx = parentIdx #curValue is now present in parentIdx
            parentIdx = (currentIdx - 1) // 2 #calculate new parentIdx

            
    # O(log(n)) time , O(1) space
    def siftDown(self, currentIdx, endIdx, heap):
        childOne = currentIdx * 2 + 1 #calculate childOneIdx i.e (2i + 1)
        #while childOne is a valid child inside bounds of the array
        while childOne <= endIdx:
            #calculate childTwo if its valid child else initialize it to '-1'
            childTwo = (2 * currentIdx + 2) if 2*currentIdx+2 <= endIdx else -1

            #now check which of the two childs have the smallest value
            if childTwo != -1 and heap[childTwo]["num"] < heap[childOne]["num"]:
                idxToSwap = childTwo
            else:
                idxToSwap = childOne

            #compare that child's value with its parent node
            if heap[idxToSwap]["num"] < heap[currentIdx]["num"]:
                self.swap(idxToSwap, currentIdx, heap)
                currentIdx = idxToSwap
                childOne = currentIdx * 2 + 1
            else: #if that child's value > parent node,
                return #no need to further perform siftDown, so return
                
    def swap(self, one, two, heap):
        heap[one], heap[two] = heap[two], heap[one]


# Input
arrays = [[1,5,8,21],[-1,0],[-125,81,121],[3,6,12,20,160]]
print(mergeSortedArrays(arrays))
# output: [-125, -1, 0, 1, 3, 5, 6, 8, 12, 20, 21, 81, 121, 160]
