# Binary Search
# Array needs to be sorted

# Solution : Using Iterative approach
# Half of the array is eliminated in each round

# Time:O(log(n)) , Space:O(1)
# where, n is no. of elements in input array

def binarySearch(array, key):
    lb = 0
    ub = len(array)-1
    while lb <= ub:
        mid = (lb + ub) // 2
        if array[mid] == key:
            return mid
        elif key > array[mid]:
            #if search element is > mid element, eliminate left half of array
            lb = mid + 1 
        else:
            #if search element is < mid element, eliminate right half of array
            ub = mid - 1
    #if element not found,
    return -1


# sorted array
array = [10,20,30,40,50,60]
key = 10
result = binarySearch(array, key)
print("Array:",array)
print("\nSearch element:",key)
print("Index value:",result)

key = 80
result = binarySearch(array, key)
print("\nSearch element:",key)
print("Index value:",result)
