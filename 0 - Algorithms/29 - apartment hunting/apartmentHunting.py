# Apartment Hunting

# Write a function that takes in a list of blocks and a list of your required buildings
# and that returns the location (the index) of the block that is most optimal for you.
'''
Explanation:

To move into a new apartment, given a list of blocks where,
each block contains an apartment that you could move into.
In order to pick your apartment, you have a list of requirements:
a list of buildings that are important to you.
For example, you might value having a school and a gym near your apartment.
The list of blocks that you have contains information at every block about all of the buildings
that are present and absent at the block in question. For instance, for every block,
you might know whether a school, a store, an office, and a gym are present or not.
You want to minimize the farthest distance you would have to walk/travel
from your apartment to reach all of your required buildings.
'''

'''
# Solution 1 : Brute Force
# Time: O(b^2 * r) , Space: O(b)
#where 'b' is no. of blocks and 'r' is no. of requirements

def apartmentHunting(blocks, requirements):
    maxDistances = [float("-inf") for block in blocks]
    for i in range(len(blocks)):
        for req in requirements:
            closestDistance = float("inf")
            for j in range(len(blocks)):
                if blocks[j][req]:
                    closestDistance = min(closestDistance, getDistance(i, j))
            maxDistances[i] = max(maxDistances[i], closestDistance)
    return getIndexOfMinValue(maxDistances)                

def getDistance(i, j):
    return abs(i - j)

def getIndexOfMinValue(array):
    minValue = float("inf")
    idx = 0
    for i in range(len(array)):
        currentVal = array[i]
        if currentVal < minValue:
            minValue = currentVal
            idx = i
    return idx
'''

# Solution 2 : By pre-computing requirements
# Time: O(b * r) , Space: O(b * r)
#where 'b' is no. of blocks and 'r' is no. of requirements
'''
We pre-compute all of the nearest gyms, schools, and stores for each block.
For example: "minDistancesOfAllReqs" - variable name used for coding
Gym:    [1, 0, 0, 1, 2] - here, nearest gym at block '0' is '1' distance away
School: [0, 1, 0, 0, 0] - here, nearest school at block '1' is '1' distance away
Store:  [4, 3, 2, 1, 0] - here, nearest store at block '1' is '3' distance away
All these above values will be stored inside a list named 'minDistancesOfAllReqs'
minDistancesOfAllReqs = [ [gym...], [school...], [store...] ]

Now, after we have pre-computed all the minimum distances of each requirement at every block,
we can create a list which stores max value found at every block for any requirement.
Like, at block '0' we have distances, gym = 1, school = 0, store = 4. So max value is '4'.
That means we have to travel maximum '4' distance to reach our requirement gym, school, etc.
We need apartment in a block that minimizes the maximum distance to travel for our requirements.

Finally we get, [4, 3, 2, 1, 2] - "maxDistancesOfBlock" - variable name used for coding
these are the max distance found for each block from their pre-computed minimum distances
In this list, '1' is the smallest value/distance that we need to travel for our requirements.
So block '3' (ie. index val) which contains distance '1' is the location for our apartment.
Output : 3
'''

def apartmentHunting(blocks, requirements):
    #for each requirement, we call getMinDistance() which returns a list of min distances
    #we need to travel for that particular requirement(for ex: gym) at each block
    #we append this list to 'minDistancesOfAllReqs' list
    minDistancesOfAllReqs = list(map(lambda req: getMinDistance(blocks, req), requirements))
    maxDistancesOfBlock = getMaxDistance(blocks, minDistancesOfAllReqs)
    return getIndexOfMinValue(maxDistancesOfBlock)

def getMinDistance(blocks, req):
    minDistances = [0 for block in blocks]
    #we initialize 'closestIdxOfReq' to "inf" so that in 1st loop from left to right,
    #if any req such as gym is absent in any block then its distance will be not defined
    #If we initialize it to '0' then even if it absent, its distance will be set to '0'
    closestIdxOfReq = float("inf")
    #looping from left to right
    for i in range(len(blocks)):
        if blocks[i][req]:
            closestIdxOfReq = i
        minDistances[i] = getDistance(i, closestIdxOfReq)
    #looping from right to left
    for j in reversed(range(len(blocks))):
        if blocks[j][req]:
            closestIdxOfReq = j
        minDistances[j] = min(minDistances[j], getDistance(j, closestIdxOfReq))
    return minDistances

def getMaxDistance(blocks, minDistancesOfAllReqs):
    maxDistances = [0 for block in blocks]
    for i in range(len(blocks)):
        #minDistancesOfAllReqs = [ [gym...], [school...], [store...] ]
        #Ex: at block '0' we have distances, gym = 1, school = 0, store = 4
        #For block '0', minDistanceAtBlock = [1, 0, 4]
        #for each block, minDistanceAtBlock stores all min values of requirements
        minDistanceAtBlock = list(map(lambda distance: distance[i], minDistancesOfAllReqs))
        #then we extract the max value from minDistanceAtBlock and store it in maxDistances[i]
        maxDistances[i] = max(minDistanceAtBlock)
    return maxDistances

def getIndexOfMinValue(array):
    minValue = float("inf")
    idx = 0
    for i in range(len(blocks)):
        currentVal = array[i]
        if currentVal < minValue:
            minValue = currentVal
            idx = i
    return idx

def getDistance(a, b):
    return abs(a - b)
    
blocks = [
            {"gym": False, "school": True, "store": False},
            {"gym": True, "school": False, "store": False},
            {"gym": True, "school": True, "store": False},
            {"gym": False, "school": True, "store": False},
            {"gym": False, "school": True, "store": True},
        ]
requirements = ["gym", "school", "store"]

print(apartmentHunting(blocks, requirements)) #ans = 3
