# Calculate sum of all elements in the given array
# and return (sum * multipler) where multipler=1
# multiplier+=1 if there is sub-array inside array

# Solution: Using Recursion

# Time:O(n) , Space:O(d)
# where, n is all the elements including each elements of sub-arrays
# and d is the largest depth into the sub-array

def productOfSum(array, multiplier=1):
    sum = 0
    for item in array:
        if type(item) is list:
            sum += productOfSum(item, multiplier+1)
        else:
            sum += item
    return sum * multiplier


array = [5,2,[7,-1],3,[6,[-13,8],4]]
# ans = 12
ans = productOfSum(array)
print(array)
print("Result = ",ans)
