# Two Number Sum
# Find [x,y] such that x + y = targetSum
# Using two for loops
# Time:O(n^2) , Space:O(1)

def twoNumberSum(array,targetSum):
    for i in range(len(array)-1):
        firstNum = array[i]
        for j in range(i+1,len(array)):
            secondNum = array[j]
            if firstNum+secondNum == targetSum:
                return [firstNum,secondNum]
    return []


#Array of distinct elements
array = [-2,10,5,-3,7,11,4,1]
targetSum = 4
# ans = [7,-3] or [-3,7]
print(twoNumberSum(array,targetSum))
