# Longest Peak

#Given an array of integers, find the length of the longest peak.
#Peak is atleast three consecutive integers, which if we read from left to right,
#values are strictly increasing until it reaches some largest value among them, then they become strictly decreasing.
'''
Example 1:
  5
 / \
4   4
This is a peak [4,5,4] of length of 3.

Example 2:
[1,2,3,3,10,9,8,-1,-2,-2,-2,6,4]
        / \ 
            \
              \
                \
                   \
Longest peak = [3,10,9,8,-1,-2]
Length of longest peak is 6.
Duplicate/same values are not allowed.
'''

# Solution : O(n) time , O(1) space
# where n is no. of elements in array
#we might revisit some elements almost 2 or 3 times that makes O(2n)|O(3n) == O(n) time
'''
We start from i=1 beacuse atleast 3 elements are needed for peak.
i.e., array[i-1] < array[i] and array[i] > array[i+1]
So We don't visit last element. We end the loop when we visit last 2nd element of array.  
If we have only increasing or decreasing values in array, then there is no peak.
'''
def longestPeak(array):
    maxLength = 0
    i = 1
    while i < len(array)-1:
        #first we find the peak
        isPeak = array[i-1] < array[i] and array[i] > array[i+1]

        if not isPeak:
            i += 1
            continue

        #if we found tip of the peak, expand to the left and right direction
        leftIdx = i - 2
        #while it is strictly decreasing to the left side
        while leftIdx >= 0 and array[leftIdx] < array[leftIdx + 1]: 
            leftIdx -= 1
        rightIdx = i + 2
        #while it is strictly increasing to the right side
        while rightIdx < len(array) and array[rightIdx] < array[rightIdx - 1]: 
            rightIdx += 1

        currentPeakLength = rightIdx - leftIdx - 1
        maxLength = max(maxLength, currentPeakLength)
        #when values are strictly decreasing, we can't find any peak values there so,
        #currently, rightIdx points to the element, which was not strictly decreasing,
        #so we continue to find peak in the array starting from where rightIdx is pointing
        i = rightIdx
    return maxLength


array = [1,3,1,1,1,4,3,2,1] #[1,4,3,2,1] , ans = 5
print(array)
print("\nLongest Peak Length =",longestPeak(array))
