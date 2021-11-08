# Binary Search
# Array needs to be sorted

# Solution : Using Recursion
# Half of the array is eliminated in each round

# Time:O(log(n)) , Space:O(log(n))
# where, n is no. of elements in input array

def binarySearch(array, key):
    return binarySearchHelper(array, key, 0, len(array)-1)

def binarySearchHelper(array, key, lb, ub):
    if lb > ub:
        #if element not found,
        return -1

    mid = (lb + ub) // 2
    if array[mid] == key:
        return mid
    elif key > array[mid]:
        #if search element is > mid element, eliminate left half of array
        return binarySearchHelper(array, key, mid+1, ub)
    else:
        #if search element is < mid element, eliminate right half of array
        return binarySearchHelper(array, key, lb, mid-1)


# sorted array
array = [10,20,30,40,50,60]
key = 20
result = binarySearch(array, key)
print("Array:",array)
print("\nSearch element:",key)
print("Index value:",result)

key = 99
result = binarySearch(array, key)
print("\nSearch element:",key)
print("Index value:",result)
