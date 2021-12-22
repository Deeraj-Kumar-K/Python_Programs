# Smallest Difference
# Given two integer arrays, return pair of two numbers [num1, num2] such that,
#num1 comes from arrayOne and num2 comes from arrayTwo with smallest difference.
'''
Example:
array1 = [-1,5,10,20,28,3], array2 = [26,134,135,15,17]
Output: [28, 26]
28 - 26 = 2 (smallest difference)
'''

'''
# Solution 1: Using two loops
# O(n^2) time | O(1) space

#This alorithm is not efficient since we generate all possible pairs.
def smallestDifference(array1, array2):
    smallest = float('inf')
    res = [0, 0] #initializing array with 2 zeroes
    for i in range(len(array1)):
        for j in range(len(array2)):
            currDiff = abs(array1[i] - array2[j])
            if currDiff == 0:
                return [array1[i], array2[j]]
            elif smallest > currDiff:
                smallest = currDiff
                res[0] = array1[i]
                res[1] = array2[j]
    return res
'''

# Solution 2: Using two pointers
# O(nLog(n) + mLog(m)) time | O(1) space
# where n is length of array1 and m is length of array2

def smallestDifference(array1, array2):
    #sorting both arrays in-place
    array1.sort()
    array2.sort()
    idxOne = 0
    idxTwo = 0
    current = float('inf')
    smallest = float('inf')
    smallestPair = []
    
    #Both pointers take roughly O(n+m) time which doesn't effect overall time complexity.
    #if one of the array reaches end, we can stop the loop, no need to check remaining array.
    while idxOne < len(array1) and idxTwo < len(array2): 
        firstNum = array1[idxOne]
        secondNum = array2[idxTwo]
        if firstNum < secondNum:
            current = secondNum - firstNum
            idxOne += 1 #if we increase idxTwo, difference will be even greater
        elif secondNum < firstNum:
            current = firstNum - secondNum
            idxTwo += 1 #if we increase idxOne, difference will be even greater
        else:
            return [firstNum, secondNum]

        if smallest > current:
            smallest = current
            smallestPair = [firstNum, secondNum]
    return smallestPair
    

array1 = [-1,5,10,20,28,3]
array2 = [26,134,135,15,17]
print(smallestDifference(array1, array2))
