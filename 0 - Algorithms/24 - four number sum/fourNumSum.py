# Four Number Sum
# Find list of all quadruplets [x,y,z,k] such that x+y+z+k = targetSum
'''
Example:
nums = [7, 6, 4, -1, 1, 2], targetSum = 16
Output: [[7,6,4,-1], [7,6,1,2]]


Solution 1: Using four loops (naive solution)
Trying all combinations to get the result
Time complexity: O(n^4) , not efficient

###########################################################################3

Solution 2: Using hash table
# Avg case Time : O(n^2) , Space: O(n^2)
# Worst case Time : O(n^3) , Space: O(n^2)
#the analysis of time and space is complex

We can divide x,y,z,k into two pairs 'P' and 'Q', where P=x+y and Q=z+k
WE have reduced our problem to a variation of Two number sum problem.
Like two number sum, we can use hashtable to store all value of 'P' along with its pairs [x,y]
{ P : [x, y] }
Ex: P=10, hashTable={ 10: [[5,5], [8,2], [7,3]] }

First we calculate Q=z+k i.e, currentNum 'z' will be added to all k values to the right of 'z'.
For each value of 'Q', we calculate the difference = (targetSum - 'Q')
If difference value 'P' is present in hashTable then return all four numbers, otherwise do nothing.

Now we will add currentNum 'z' with all values to the left of 'z' in the array.
If currentSum 'P' is in hashtable then append the pairs [x,y] to it, if not, create new entry

We store the currentSum and its pair into hashtable when we reach the 2nd element of the pair.
We store values in this manner to avoid duplicate answers such as [x,y,z,k], [y,x,z,k], [k,x,y,z], etc.
'''

def fourNumberSum(array, targetSum):
    
    allPairSums = {} #our hashtable
    res = [] #to store quadruplets
    
    #1st element 'z' will be added with all numbers but we will not get any result coz hashtable is empty.
    #last element has no element ahead of it so we can't perform Q=z+k
    #so, first and last elements are excluded in the loop because no operation will be done with them
    
    for i in range(1, len(array) - 1): 
        for j in range(i + 1, len(array)):
            currentSum = array[i] + array[j]
            difference = targetSum - currentSum
            if difference in allPairSums: #if we have 'P' in hashtable corresponding to current value of 'Q'
                for pair in allPairSums[difference]: #then for each pair [x,y] in {P:[x,y]}
                    res.append(pair + [array[i] , array[j]] ) #append [x,y,z,k] into result array

        #looping to the left of current number to store 'P' and its pairs [x,y] into hashtable
        for k in range(0, i): #value 'i' is excluded because it will be added with all numbers to the left of it
            currentSum = array[i] + array[k]
            if currentSum not in allPairSums:
                allPairSums[currentSum] = [ [array[k], array[i]] ] #creating new entry { P: [x, y] }
            else:
                allPairSums[currentSum].append( [array[k], array[i]] )
                
    return res

    
#Array of distinct elements
nums = [7,6,4,-1,1,2]
targetSum = 16
print(fourNumberSum(nums, targetSum))
