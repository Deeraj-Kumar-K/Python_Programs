# Two Number Sum
# Find [x,y] such that x + y = targetSum
# Using Hash table
# Time:O(n) , Space:O(n)

def twoNumberSum(array,targetSum):
    nums={}
    for x in array:
        # x+y=sum then y=sum-x
        y = targetSum - x
        if y in nums:
            return [x,y]
        else:
            nums[x]=True
    return []


#Array of distinct elements
array = [-2,10,5,-3,7,11,4,1]
targetSum = 4
# ans = [7,-3] or [-3,7]
print(twoNumberSum(array,targetSum))
