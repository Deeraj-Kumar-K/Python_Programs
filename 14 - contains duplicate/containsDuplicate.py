# Contains Duplicate
# Given an integer array, return true if any value appears at least twice
# in the array, and return false if every element is distinct.
'''
Input: [1,4,5,1]
Output: true

Input: [1,2,3,4]
Output: false
'''

def containsDuplicate(array):
        hashTable = {}
        left = 0
        right = len(array)-1
        while(left < right):
            #if duplicate element is present, return true
            if array[left] in hashTable:
                return True
            #else, add that element into hashtable
            else:
                hashTable[array[left]] = True
                
            # Similarly repeat above steps here  
            if array[right] in hashTable:
                return True
            else:
                hashTable[array[right]] = True
            
            left+=1
            right-=1
        return False


array = [1,4,5,1]
print(array)
print(containsDuplicate(array))
array = [1,2,3,4]
print(array)
print(containsDuplicate(array))
