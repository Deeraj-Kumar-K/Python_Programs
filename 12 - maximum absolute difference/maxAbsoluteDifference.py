# https://www.hackerrank.com/challenges/30-scope/problem

# Maximum absolute difference between two integers in a set of +ve integers
# is the largest absolute difference between any two integers in the array 
'''
Sample Input:
STDIN   Function
-----   --------
3       size of __elements[] is N = 3
1 2 5   __elements = [1, 2, 5]

Sample Output:
4
'''
class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = None
        
    def computeDifference(self):
        left = 0
        right = len(self.__elements)-1
        elements = sorted(self.__elements)
        if left == right:
            self.maximumDifference = elements[0]
        else:
            self.maximumDifference = abs(elements[right] - elements[left])
            

_ = input()
a = [int(e) for e in input().split(' ')]
d = Difference(a)
d.computeDifference()
print(d.maximumDifference)
