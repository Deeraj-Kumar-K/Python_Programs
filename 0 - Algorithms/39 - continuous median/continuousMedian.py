# Continuous Median

# Create a class that supports the following two functionalities:
# 1. continuous insertion of numbers and 2. instant (O(1) time) retrieval
# of the median of numbers that have been inserted until then.
'''
Explanation:

Suppose we have 3 nos, [5, 10, 100] then median is the middle number.
So median = 10. But if we have even number of elements,
Ex: [5,10,100,200] then median is the average of the middle numbers,
i.e average of 10 and 100. So median = (10 + 100) / 2 = 55

Note:
Every time we insert a number, that number should be in its sorted place.

For ex, we have an empty array [].
We insert 5, Array = [5] and median = 5.
We insert 10, Array = [5,10] and median = (5 + 10) = 7.5
We insert 100, Array = [5,10,100] and median = 10 
We insert 200, Array = [5,10,100,200] andmedian = (10 + 100) / 2 = 55
We insert 6, Array = [5,6,10,100,200] and median = 10
Here, we can see, '6' is inserted in sorted position and then we find median.


Approach 1: Using Insertion sort
We insert each number in its sorted place using Insertion sort
Each insertion of number will take O(n) time.


Approach 2: Using Min and Max heap # O(log(n)) time , O(n) space
We divide the array into two heaps ie. lowerhalf and greaterhalf
lowerHalf uses MAX heap and greaterHalf uses MIN heap.

Ex: lowerHalf = [5] greaterHalf = [] , then median = 5
lowerHalf = [5] greaterHalf = [10] , then median = (5 + 10) / 2 = 7.5
lowerHalf = [5] greaterHalf = [10, 100], median = 10
now we have odd no. of elements, and since greaterHalf is min heap,
and has more no. of elements so take its root value i.e 10 as median.

lowerHalf = [5] greaterHalf = [10, 100, 200], now rebalance the heaps
we get lowerHalf = [5 , 10] greaterHalf = [100, 200]
lowerHalf is Max heap, and now we have even no. of elements coz both heaps
have equal length, so take average of root elements, (10 + 100) / 2 = 55
median = 55.

Lets take above example,
We insert 5, it check lowerHalf is empty and inserts there, median = 5.
We insert 10, 10 > 5, so insert in greaterHalf, length of heaps are equal
so median = 5 + 10 / 2 = 7.5
We insert 100, 100 > 5 so insert in greaterHalf.
Right now lowerHalf root = 5 and greaterhalf root = 10
Length of greaterHalf > lowerHalf i.e 2 > 1, so median = 10 which is root value.
We insert 200, 200 > 5 so insert in greaterHalf.
Now greater half has 3 elements, and lowerHalf has 1 element so rebalance heaps.
Then calculate median, so we get median = 55.


# Time and Space Complexity:

# insert() of class ContinuousMedianHandler does 3 operations:
1st insert number in heap i.e O(log(n)) time
2nd rebalanceHeaps() which in turn has insert()/remove() of heap
those operations are also O(log(n)) time.
3rd updateMedian() which is constant time operation.
So overall time complexity  is O(log(n)) time.

# O(n) space is used because both min / max heap together stores 'n' elements.
'''

def MAX_HEAP_FUNC(a, b):
        return a > b

def MIN_HEAP_FUNC(a, b):
        return a < b
    
class ContinuousMedianHandler:
    def __init__(self):
        self.lowerHalf = Heap(MAX_HEAP_FUNC, [])
        self.greaterHalf = Heap(MIN_HEAP_FUNC, [])
        self.median = None

    # O(log(n)) time , O(n) space
    def insert(self, number):
        #if lowerHalf heap is empty or currentNum < root of lowerHalf,
        if not self.lowerHalf.length or number < self.lowerHalf.peek():
            self.lowerHalf.insert(number) # then insert into lowerHalf
        else:
            self.greaterHalf.insert(number) # else insert into greaterhalf
        self.rebalanceHeaps() # after inserting, rebalance the heaps
        self.updateMedian() # then calculate the current median

    # O(log(n)) time , O(1) space
    def rebalanceHeaps(self):
        #if lowerHalf have 2 extra elements than greaterhalf,
        #then remove top element of lowerHalf and insert it into greaterHalf
        if self.lowerHalf.length - self.greaterHalf.length == 2:
            self.greaterHalf.insert(self.lowerHalf.remove())
        #if greaterhalf have 2 extra elements than lowerHalf ,
        #then remove top element of greaterHalf and insert it into lowerHalf
        elif self.greaterHalf.length - self.lowerHalf.length == 2:
            self.lowerHalf.insert(self.greaterHalf.remove())

    # O(1) time , O(1) space
    def updateMedian(self):
        # if both heaps have equal no. of elements, it means even no. of elements
        #take avgerage of top elements of both heaps
        if self.lowerHalf.length == self.greaterHalf.length:
            self.median = (self.lowerHalf.peek() + self.greaterHalf.peek()) / 2
        #if odd number of elements, then return root value of heap
        #that contains more elements
        elif self.lowerHalf.length > self.greaterHalf.length:
            self.median = self.lowerHalf.peek()
        else:
            self.median = self.greaterHalf.peek()
            
    # O(1) time , O(1) space
    def getMedian(self):
        return self.median
      
    
class Heap: #contains both MIN heap and MAX heap
    def __init__(self, comparison, array):
        self.heap = self.buildHeap(array) #building heap from input array
        self.length = len(self.heap) #stores current no. of elements in heap
        self.comparison = comparison #determines if min heap or max heap

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
        return self.heap[0] #root

    def showHeap(self):
        return self.heap


    # O(log(n)) time , O(1) space
    def insert(self, value):
        self.heap.append(value) #new value is inserted at last position
        self.length += 1 # update the no. of elements in heap
        self.siftUp(self.length - 1, self.heap) #then perform siftUp


    # O(log(n)) time , O(1) space
    def remove(self):
        #first swap root element with last element in heap
        self.swap(0, len(self.heap) - 1, self.heap)
        valueToRemove = self.heap.pop() #then pop the last element
        #now siftDown the new root element to its correct place in heap
        self.length -= 1 # update no.of elements in heap
        self.siftDown(0, self.length - 1, self.heap)
        return valueToRemove #return the min/max value of heap


    # O(log(n)) time , O(1) space
    def siftUp(self, currentIdx, heap):
        parentIdx = (currentIdx - 1) // 2
        
        #loop breaks if we reach the root node while performing siftUp
        #coz we can't siftUp the root element
        
        while currentIdx > 0:
            # if currentIdx < parentIdx, for MIN Heap and
            # if currentIdx > parentIdx, for MAX Heap
            if self.comparison(heap[currentIdx], heap[parentIdx]):
                self.swap(currentIdx, parentIdx, heap)
                currentIdx = parentIdx #curValue is now present in parentIdx
                parentIdx = (currentIdx - 1) // 2 #calculate new parentIdx
            else:
                return

            
    # O(log(n)) time , O(1) space
    def siftDown(self, currentIdx, endIdx, heap):
        childOne = currentIdx * 2 + 1 #calculate childOneIdx i.e (2i + 1)
        #while childOne is a valid child inside bounds of the array
        while childOne <= endIdx:
            #calculate childTwo if its valid child else initialize it to '-1'
            childTwo = (2 * currentIdx + 2) if 2*currentIdx+2 <= endIdx else -1

            if childTwo != -1:
                #if childOne < childTwo, for MIN Heap and
                # if childOne > childTwo, for MAX Heap
                if self.comparison(heap[childTwo], heap[childOne]):
                    idxToSwap = childTwo
                else:
                    idxToSwap = childOne
            else:
                idxToSwap = childOne

            #compare that child's value with its parent node
            #for MIN Heap check, if idxToSwap < currentIdx and
            #for MAX Heap check, if idxToSwap > currentIdx
            if self.comparison(heap[idxToSwap], heap[currentIdx]):
                self.swap(idxToSwap, currentIdx, heap)
                currentIdx = idxToSwap
                childOne = currentIdx * 2 + 1
            else:
                return #no need to further perform siftDown, so return
                
    def swap(self, one, two, heap):
        heap[one], heap[two] = heap[two], heap[one]


# Input
test = ContinuousMedianHandler()
test.insert(5)
print(test.getMedian())
test.insert(10)
print(test.getMedian())
test.insert(100)
print(test.getMedian())
test.insert(200)
print(test.getMedian())
test.insert(6)
print(test.getMedian())
