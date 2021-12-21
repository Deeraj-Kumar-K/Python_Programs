# Three Number Sum
# Find list of all triplets [x,y,z] such that x+y+z = targetSum
'''
Example:
nums = [1, 2, 3, -6, -8, 5, 6, 12], targetSum = 0
Output: [[-8,2,6], [-8,3,5], [-6,1,5]]

Solution 1: Using three loops | O(n^3) time

Solution 2: Using hash table
Like we solved in two number sum, we can use hashtable to store all values
and use double for loops to find the third number in hashtable
x+y+z = sum , so we get z=sum-x-y
here extra memory is used and we can have complications coz output can have duplicates
For ex: [-8,2,6] is same as [2,-8,6], [6,-8,2], [6,2,-8], etc
'''

# Solution 3: Using left and right pointers
# Time complexity: O(n^2) , Space: O(n)
#O(n) space, we might store all numbers if every number is used in some triplet

def threeNumberSum(array, targetSum):
    #sorting with good algos take O(nlogn) time
    array.sort()
    triplets = []
    for i in range(len(array) - 2):
        currNum = array[i] #there is no need to store in separate variable, just for simplicity
        left = i+1
        right = len(array)-1
        while left < right:
            currSum = currNum + array[left] + array[right]
            if currSum == targetSum:
                triplets.append( [currNum, array[left], array[right]] )
                #since we need all possible triplets, we check further by moving both pointers
                #if we only increase left, our sum will surely be greater than targetSum
                #if we only decrease right, our sum will surely be less than targetSum, so
                left += 1
                right -= 1
            elif currSum < targetSum:
                left += 1
            else:
                right -= 1
    return triplets


#Array of distinct elements
nums = [1, 2, 3, -6, -8, 5, 6, 12]
targetSum = 0
print(threeNumberSum(nums, targetSum))
