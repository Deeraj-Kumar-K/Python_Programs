# Selection Sort (in-place)
# Find smallest element in the array and swap it with 1st element
# find 2nd smallest element and swap it with 2nd element and so on.

# Time:O(n^2) , Space:O(1)

def selectionSort(array):
    currentIdx = 0
    #when every element will be placed in their sorted place,
    #we don't need to check the last element
    while(currentIdx < len(array)-1): #thats why len(array)-1 
        smallestIdx = currentIdx
        for i in range(currentIdx+1, len(array)):
            if array[smallestIdx] > array[i]:
                smallestIdx = i
                #smallestIdx points to index of smallest value found                
        #after finding smallest number, swap it        
        swap(currentIdx, smallestIdx, array)
        currentIdx += 1
    return array

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]


array = [20,30,50,10,40]
print("Before sorting:",array)
result = selectionSort(array)
print("\nAfter sorting:",result)
        
