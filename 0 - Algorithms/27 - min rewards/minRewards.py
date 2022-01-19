# Minimum Rewards
# Given an array of integers, which represents the list of scores of students in exam.
# We being the teacher, have to reward each student atleast one reward.
# Reward can be anything such as candy or coins.
# A student with lower score than the next student should have fewer reward than the next student
# Similarly student with  higher score will have more rewards than its neighbour.
# Return the sum of minimum no. of rewards to give according to the given conditions.
'''
Constraints:
They are only positive integers.
No duplicate values/grades. Otherwise algorithm will be complex.
Order of scores matter. So we cannot sort the array.

##########################################################

Example:
Input : [8,4,2,1,3,6,7,9,5]

Rewards: [4,3,2,1,2,3,4,5,1]
Adding all values of rewards we get 25.

Output: 25
'''

'''
# Solution 1 : Naive Solution
# O(n^2) time , O(n) space

def minRewards(scores):
    rewards = [1 for _ in scores] #initializng the array with '1'
    for i in range(1, len(scores)):
        j = i - 1
        if scores[i] > scores[j]: #if i'th student score > prev student, 
            rewards[i] = rewards[j] + 1
        else:
            #we have to loop backwards and change reward values
            while j >= 0 and scores[j] > scores[j+1]:
                rewards[j] = max(rewards[j], rewards[j+1] + 1)
                j -= 1
    print("Rewards:",rewards)
    return sum(rewards)


# Solution 2 : By finding all local mins in the array and then expanding to left and right
# O(n) time , O(n) space

def minRewards(scores):
    rewards = [1 for _ in scores]
    localMinIdxs = getLocalMinIdxs(scores) #stores the index values of all local min values
    for localMinIdx in localMinIdxs:
        expandToLeftAndRight(localMinIdx, scores, rewards)
    return sum(rewards)

#helper function to get all index values of local min values
def getLocalMinIdxs(array):
    if len(array) == 1: #if only one element in the array
        return [0] #return index '0'
    localMinIdxs = []
    for i in range(len(array)):
        if i == 0 and array[i] < array[i + 1]: #edge case: if 1st element
            localMinIdxs.append(i)
        if i == len(array) - 1 and array[i] < array[i - 1]: #edge case: if last element
            localMinIdxs.append(i)
        if i == 0 or i == len(array) - 1: #if above 2 cases not executed
            continue
        if array[i] < array[i + 1] and array[i] < array[i - 1]:
            localMinIdxs.append(i)
    return localMinIdxs

def expandToLeftAndRight(localMinIdx, scores, rewards):
    leftIdx = localMinIdx - 1
    while leftIdx >=0 and scores[leftIdx] > scores[leftIdx + 1]:
        rewards[leftIdx] = max(rewards[leftIdx], rewards[leftIdx + 1] + 1)
        leftIdx -= 1
    rightIdx = localMinIdx + 1
    while rightIdx < len(scores) and scores[rightIdx] > scores[rightIdx - 1]:
        #rewards[rightIdx] = max(rewards[rightIdx], rewards[rightIdx - 1] + 1)
        #here, we can skip the max condition as shown above because
        #when we go from left to right, those values get changed for the first time
        #but when we go from right to left, we have to check for max value
        rewards[rightIdx] = rewards[rightIdx - 1] + 1 
        rightIdx += 1
'''    

# Solution 3 : By iterating from left to right and right to left
# O(n) time , O(n) space

def minRewards(scores):
    rewards = [1 for _ in scores]
    for i in range(1, len(scores)): #first value in array is ignored
        if scores[i] > scores[i - 1]:
            rewards[i] = rewards[i - 1] + 1
    for i in reversed(range(len(scores) - 1)): #last value in array is ignored
        if scores[i] > scores[i + 1]:
            rewards[i] = max(rewards[i], rewards[i + 1] + 1)
    return sum(rewards)

    
scores = [8,4,2,1,3,6,7,9,5]
print(scores)
print("Sum of Rewards:",minRewards(scores)) #ans =25
