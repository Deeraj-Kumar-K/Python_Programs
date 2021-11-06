# Insertion Sort
# (in-place sorting, no need for helper array)
# Assume 1st element(index 0) is sorted, check other elements one by one
# Insert them to their sorted place by looping backwards

# Time:O(n^2) , Space:O(1)
# where n is no. of elements in the list

def insertionSort(array):
    # looping forward for checking elements 1-by-1
    for i in range(1,len(array)):
        j=i
        #looping backwards to insert current element in its sorted place
        while j>0 and array[j]<array[j-1]:
            swap(j, j-1, array)
            j -= 1
    return array
            
# helper function for swapping
def swap(i, j, array):
    array[i], array[j] = array[j], array[i]


array = [3,2,5,4,1]
print("Before soring:",array)
insertionSort(array)
print("\nAfter sorting:",array)
