# Construct Min Heap

# Create a Min Heap class that supports building the heap from an input array.
# It should also support insertion, removal, peeking of the root / min value.
# Also supporting sifting a value up and down the heap.
# Represent the heap in the form of an array.
'''
Explanation:

Heap is a binary tree. It can be represented in the form of an array.
In min heap, every node has a value that is less than its child nodes.
So the root node will have the least value in the min heap.
It is the opposite in max heap.

Min heap : [8, 12, 23, 17, 31, 30, 44, 103]

       8
      / \
    12   23
    / \  / \
   17 31 30 44
  /  
103        

The elements are stored from left to right. So all the levels will
have full elements except the last level.

Formulae:
currentNode = i
childOne = 2 * i + 1
childTwo = 2 * i + 2
parentNode = floor((i - 1) / 2)

So for constructing min heap, we need the following operations:
- Build Heap : building the heap from an input array
- Sift Down : if parent's value > child nodes, swap it with smaller child
- Sift Up : when child node's value < parent node, swap them
- Insert : insert a new value into the heap
- Remove : pop/remove the (root / min value) from heap

Note: Heap represented in array form is not a sorted array.
Elements in the heap will be present in any order, not in sorted order.

# Time and Space Complexity:

Functions like insert, remove, siftUp and siftDown take O(log(n)) time
because after every operation, half of the tree is ignored/skipped.

The buildHeap() function takes O(n) time coz we use "siftDown".
It looks like it might take O(nlog(n)) time but thats not the case.

Because majority nodes of the binary tree are present in the bottom region,
and so the "siftDown" operation doesn't take much time with them.
It takes O(log(n)) time with only the root element.
Because it may have to siftDown the root element to the bottom of the tree.

With elements in the last row or last second row of the binary tree,
it will take constant time for siftDown operation.
So overall, the buildHeap() takes O(n) time.

If we use "siftUp" to build heap then it takes O(nlog(n)) time.
Because we will start from top/root element till end of the heap.
And all the 'n' elements (except root element) will take almost O(log(n)) time.
So we get a time complexity of O(nlog(n)) time.

# O(1) space because swapping is done in-place and no extra memory used.
'''

class MinHeap:
    def __init__(self, array):
        self.heap = self.buildHeap(array) #building heap from input array

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
        
        while currentIdx > 0 and heap[currentIdx] < heap[parentIdx]:
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
            if childTwo != -1 and heap[childTwo] < heap[childOne]:
                idxToSwap = childTwo
            else:
                idxToSwap = childOne

            #compare that child's value with its parent node
            if heap[idxToSwap] < heap[currentIdx]:
                self.swap(idxToSwap, currentIdx, heap)
                currentIdx = idxToSwap
                childOne = currentIdx * 2 + 1
            else: #if that child's value > parent node,
                return #no need to further perform siftDown, so return
                
    def swap(self, one, two, heap):
        heap[one], heap[two] = heap[two], heap[one]


# Input
test = MinHeap([1, 2, 3, 4, 5, 6, 7, 8])
print(test.showHeap())
# heap = [1, 2, 3, 4, 5, 6, 7, 8]
test.remove() #root/min val = '1' is removed
print(test.peek()) # (root / min val) = 2
test.insert(999)
test.insert(1)
print(test.peek()) # (min val / root) = 1
print(test.showHeap())
# heap = [1, 2, 3, 4, 5, 6, 7, 999, 8] #heap is not a sorted array
