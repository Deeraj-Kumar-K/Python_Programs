# Underscore Substring

# Given two strings: a main string and a substring of the main string.
# Return a version of the main string such that every instance of the
# substring in it is placed between underscores ("_").
# If two instances of the substring in the main string overlap each other
# or sit side by side, the underscores relevant to these two substrings
# should only appear on the far left of the left substring and on the
# far right of the right substring.
# If the main string does not contain the substring, return the main string.
'''
Explanation:

string = "Its a test to check if it works"
substring = "test"
Output = "Its a _test_ to check if it works"
The substring "test" is placed between underscores in the main string.

string = "testthis is a testtest to check if testestest it works"
substring = "test"
Output = "_test_this is a _testtest_ to check if _testestest_ it works"

here, substring "test" sit side by side ("testtest") in main string and
it also overlaps ("testestest")


# Time and Space Complexity:

# We traverse the string which is O(n) time.
At each index we call the find(subString) method which takes O(n + m) time,
where 'n' is the lenth of main string and 'm' is the length of substring.
So overall we get, O(n(n + m)) = O(n^2 + n*m) time.

# O(n) space because even at worst case where we might have to put underscores
after every character, Ex: string = "gagagag", subStrig = "g"
Output = "_g_a_g_a_g_a_g_"
We get a new string of atmost length (2 * n), which is O(n) space.

'''

# O(n^2 + n * m) time , O(n) space
# where 'n' is the lenth of main string and 'm' is the length of substring

def underscorifySubstring(string, subString):
    locations = collapse(getLocations(string, subString)) #idxs where underscores will be inserted
    return underscorify(string, locations) # insert underscores in string

def getLocations(string, subString):
    startIdx = 0
    locations = []
    while startIdx < len(string):
        subStringIdx = string.find(subString, startIdx) # find substring in string from startIdx to end
        if subStringIdx != -1: # if subString is found,
            locations.append( [subStringIdx, subStringIdx + len(subString)] ) # append its index location
            startIdx = subStringIdx + 1 # now search for next substring
        else:
            #if substring not found, then break the loop
            break
    return locations

def collapse(locations):
    if not len(locations): # if locations arr is empty
        return locations

    newLocations = [ locations[0] ] # initialize newLocations
    previous = newLocations[0] # previous pointer points to prevLocation. Overlapping locations can be collapsed.
    # if previous pointer is updated, then the values inside newLocations will also be updated
    
    for i in range(1, len(locations)):
        current = locations[i] #currentLocation[startIdx, endIdx] where underscore should be inserted
        if current[0] <= previous[1]: # if startIdx of currLocation overlaps with endIdx of prevLocation
            previous[1] = current[1] # then collapse those two locations into one location
        else:
            newLocations.append(current) # else if not overlapping, append currLocation into newLocations
            previous = current # previous pointer points to the currLocation that was append into newLocations
    # so if previous pointer is updated, the prevLocation appended to newLocations will also be updated
    return newLocations

def underscorify(string, locations):
    stringIdx = 0
    locationsIdx = 0 #Ex: locations = [[0,4], [10,14], [21,25]]
    finalChars = []
    inBetweenUnderscores = False
    i = 0 # it points to startIdx or endIdx of currentLocation
    while stringIdx < len(string) and locationsIdx < len(locations):
        if stringIdx == locations[locationsIdx][i]: #if stringIdx == idx where underscore needs to be inserted,
            finalChars.append("_") # then insert underscore
            inBetweenUnderscores = not inBetweenUnderscores # update if underscore inserted at startIdx or endIdx
            if not inBetweenUnderscores: # if underscore inserted at endIdx, it means our pointer is not in between
                locationsIdx += 1 # go to the next location where underscores need to be inserted
            i = 0 if i == 1 else 1 # if underscore inserted at startIdx then change it to endIdx and vice versa
        finalChars.append(string[stringIdx]) # keep appending characters of the string at every iteration
        stringIdx += 1
        
    if locationsIdx < len(locations): # loop ended beacuse we traversed through entire string, stringIdx < len(string)
        finalChars.append("_") # but final underscore is remaining at the end
    elif stringIdx < len(string): # here, loop ended beacuse of locationsIdx < len(locations), all locations were used
        finalChars.append(string[stringIdx : ]) # so now append all the remaining strings
        
    return "".join(finalChars) # finally return the output string        


# Input
print(underscorifySubstring("testthis is a testtest to check if testestest it works", "test"))
#output = "_test_this is a _testtest_ to check if _testestest_ it works"
