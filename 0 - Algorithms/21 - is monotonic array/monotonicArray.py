# Monotonic Array

#Given an array of integers , check if array is monotonic or not.
#Monotonic is when the numbers are in non-increasing or non-decreasing order.
#They don't have to be strictly increasing/decreasing because duplicate values are allowed.
#Ex:[1,3,50,100] - strictly increasing and monotonic
#Ex:[1,1,3,3,50,100] - not strictly increasing but monotonic
'''
Example:
Input: [10,3,0,0,0,-2,-100,-100,-999]
Output: True
It is monotonic since numbers are in non-increasing order.
'''

'''
# Solution 1 : By finding direction of array
#direction can be increasing (+ve), decreasing(-ve) or equal(zero)
# O(n) time , O(1) space

def isMonotonicArray(array):
    if len(array) <= 2:
        return True
    
    direction = array[1] - array[0]

    for i in range(2, len(array)):
        if direction == 0:
            direction = array[i] - array[i - 1]
            continue #continue until we find a direction
        #after we have found the direction i.e direction != 0,
        #check if any number breaks direction,then not monotonic array
        if breaksDirection(direction, array[i-1], array[i]):
            return False
    return True

def breaksDirection(direction, previousNum, currentNum):
    difference = currentNum - previousNum
    if direction > 0:
        return difference < 0 #returns true if direc > 0 but diff is < 0
    return difference > 0 #else if direction < 0 and difference > 0 
'''

# Solution 2 : Using two boolean values
#we check if numbers in array are increasing/decreasing together
# O(n) time , O(1) space

def isMonotonicArray(array):
    isNonIncreasing = True
    isNonDecreasing = True
    for i in range(1, len(array)):
        if array[i] > array[i - 1]: #since 2nd value is bigger,it is increasing
            isNonIncreasing = False
        if array[i] < array[i - 1]: #since 2nd value is smaller,it is decreasing
            isNonDecreasing = False
    return isNonIncreasing or isNonDecreasing
    

array = [1,2,3,50,25,100]
print(array)
print("Is Monotonic array:",isMonotonicArray(array))

array = [10,3,0,0,0,-2,-100,-100,-999]
print(array)
print("Is Monotonic array:",isMonotonicArray(array))
