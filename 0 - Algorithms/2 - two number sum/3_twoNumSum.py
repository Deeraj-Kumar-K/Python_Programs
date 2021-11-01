# Two Number Sum
# Find [x,y] such that x + y = targetSum
# Using left and right Pointers
# Time:O(nlogn) , Space:O(1)

def twoNumberSum(array,targetSum):
    #sorting with good algos take O(nlogn) time
    array.sort()
    left = 0
    right = len(array)-1
    #this while loop take O(n) time
    while left < right:
        currentSum = array[left] + array[right]
        if currentSum == targetSum:
            return [array[left],array[right]]
        elif currentSum < targetSum:
            left += 1
        else:
            right -= 1
    return []


#Array of distinct elements
array = [-2,10,5,-3,7,11,4,1]
targetSum = 4
# ans = [7,-3] or [-3,7]
print(twoNumberSum(array,targetSum))
