# Bubble Sort Algorithm (In-place sorting)
# Compare two elements and swap only if a>b

# Avg/Worst case: Time:O(n^2) , Space:O(1)
# Best case: Time:O(n) - when array is already sorted

def bubbleSort(array):
    
    isSorted = False
    #isSorted checks if there were any swaps
    #if zero swap, array is sorted otherwise continue sorting.
    
    counter = 0
    #counter helps to ignore checking of rightmost elements
    #since rightmost elements are in their sorted place.
    
    while not isSorted:
        isSorted = True
        for i in range(len(array)-1-counter):
            if array[i] > array[i+1]:
                swap(i, i+1, array)
                isSorted = False
        counter += 1
    #return array

def swap(i, j, array):
    #array[i], array[j] = array[j], array[i]
    temp = array[i]
    array[i]=array[j]
    array[j]=temp


array = [99,88,2,3,1,4,5]
print("Unsorted array:",array)

bubbleSort(array)
print("\nAfter Sorting:",array)


