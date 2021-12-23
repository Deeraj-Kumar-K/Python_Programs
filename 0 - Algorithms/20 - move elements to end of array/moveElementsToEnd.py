# Move Elements to End

#Given an array of integers and a target value,
#move all instances of the target value to the end of the array.
#You have to do this in-place and order of other elements doesn't matter.
'''
Example:
array = [5,1,5,2,3,5,5], target = 5
Output: [1,2,3,5,5,5,5] or [2,1,3,5,5,5,5] or [3,1,2,5,5,5,5], etc
Order of other elements doesn't matter.
'''

# Solution : Using two pointers
# Time: O(n) , Space: O(1)

def moveElementsToEnd(array, target):
    left = 0
    right = len(array) - 1
    while left < right:
        #find suitable position in the end to swap target value 
        #Ex: [5,1,2,4,5,5,5], target = 5
        #left points to 1st value '5' and right will point to value '4'
        while left < right and array[right] == target: #left < right is important 
            right -= 1
        #now right pointer has found suitable candidate that can be swapped
        if array[left] == target:
            array[left], array[right] = array[right], array[left]
        left += 1
    return array
        


array = [5,1,5,2,3,5,5]
target = 5
print(moveElementsToEnd(array, target))
