# Largest Range

# Given an array of integers, find the largest range of numbers in the array.
# Ex: Range of numbers [3,7] is [3,4,5,6,7]
'''
Example:

Input: [1, 12 ,3 ,0 ,16 ,5 ,2 ,4 ,13 ,7 ,14 ,6]

In the above example, we have three range of numbers,
1st: [0,1,2,3,4,5,6,7]
2nd: [12,13,14]
3rd: [16]

Largest range is [0,1,2,3,4,5,6,7], so return the start and end value of range.

Output: [0, 7]
############################################################3

Solution:
1st solution can be implemented by sorting the numbers and keeping track of the range.
Sorting takes O(nLogn) time. We can get optimal solution using hashtable.

2nd Solution, we store all values of array in the hashtable with boolean values.
We then iterate every number in the array one by one.
If currentNum is not visited i.e its boolean value is False then,
Expand its range to the extreme left and extreme right.

But if the number is already visited which means it was involved in any of the range
then, skip that number and iterate to the nex number.

Keep track of the longest range and return the final result.
'''

'''
# Solution 01 : Using sorting of numbers
# O(nLog(n)) time , O(1) space

def largestRange(array):
    array.sort()
    bestRange = []
    longestLength = 0
    currentLength = 1
    startRange = array[0] #store the value from where the range starts
    for i in range(len(array)-1):
        if array[i+1] == array[i] + 1: #if nextNum in the array == currentNum + 1
            currentLength += 1
            if currentLength > longestLength:
                longestLength = currentLength
                bestRange = [startRange, array[i + 1]]
                
        #if the range breaks i.e. if nextNum != currentNum + 1, then
        else:
            currentLength = 1 #reset value of currentLength
            startRange = array[i + 1] #store the value from where the 'next' range starts
    return bestRange
'''

# Solution 2 : Using hashtable
# O(n) time , O(n) space

def largestRange(array):
    bestRange = []
    longestLength = 0
    visited = {}

    #each number of the array is stored in hashtable and is marked false
    for num in array:
        visited[num] = False #it is false because it is not yet visited
        
    for num in array:
        if visited[num]: #skip the number if it is already visited
            continue
        
        visited[num] = True #mark the number as visited
        currentLength = 1
        
        left = num - 1
        right = num + 1
        
        #expand the range to its left
        while left in visited: #while the currentNum is in hashtable
            visited[left] = True #mark as visited
            currentLength += 1
            left -= 1

        #expand the range to its right
        while right in visited:
            visited[right] = True
            currentLength += 1
            right += 1
            
        if currentLength > longestLength:
            longestLength = currentLength
            bestRange = [left + 1, right - 1]
            
    return bestRange


array = [1, 12 ,3 ,0 ,16 ,5 ,2 ,4 ,13 ,7 ,14 ,6]
print(array)
print(largestRange(array))
print()
array = [1,2,3,4,9,8,7]
print(array)
print(largestRange(array))
