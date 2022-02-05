# Construct Min Max Stack

# Write a program consisting of a Min Max Stack class.
# It should support pushing, popping values on and off the stack,
# peeking at value at top of stack, and getting both the minimum
# and the maximum values in the stack.
# All methods should run in constant time and with constant space.

'''
Explanation:

First '5' is pushed into stack, we have Stack: [5], min:5, max:5
then '8' is pushed into stack, we have Stack: [5, 8], min:5, max:8
then '3' is pushed into stack, we have Stack: [5, 8, 3], min:3, max:8

If two variables 'min', 'max' are used to keep track of minimum/maximum number
in the stack then, if we pop the last element from stack, we no longer have
the min and max values. We would have to scan the entire stack to get them.
That will take linear time and not constant time.

So we will use a 'minMaxStack' to store and keep track of the min/max number
whenever a number is pushed into or popped from the stack.

Example:
Stack = []
minMaxStack = []

Push '5' into the stack , Stack: [5]
minMaxStack: [{'min': 5, 'max': 5}]

Push '8' into the stack , Stack: [5, 8]
minMaxStack: [{'min': 5, 'max': 5}, {'min': 5, 'max': 8}]

Push '3' into the stack , Stack: [5, 8, 3]
minMaxStack: [{'min': 5, 'max': 5}, {'min': 5, 'max': 8}, {'min': 3, 'max': 8}]

We can see that top/last element of minMaxStack has the lastest min/max values
If we pop an element from stack , we get
Stack: [5, 8]
minMaxStack: [{'min': 5, 'max': 5}, {'min': 5, 'max': 8}]
So '3' which was the top element got popped and we have min = 5, max = 8
'''

# Time complexity: O(1) , Space complexity: O(n)

class MinMaxStack: #overall O(1) time, O(3 * n) = O(n) space

    def __init__(self):
        self.stack = [] #O(n) space
        self.minMaxStack = [] #O(2 * n) space

    # O(1) time , O(1) space
    def pop(self):
        self.minMaxStack.pop() #first we pop minMaxStack's top element 
        return self.stack.pop() #then we pop the top element of stack

    # O(1) time , O(1) space
    def peek(self):
        return self.stack[len(self.stack) - 1] #return top element of stack

    # O(1) time , O(1) space
    def push(self, value):
        #initializing newMinMax with the number we are pushing into stack
        newMinMax = {"min": value, "max": value}
        if len(self.minMaxStack): #if minMaxStack is not empty
            currentMinMax = self.minMaxStack[len(self.minMaxStack) - 1]
            newMinMax["min"] = min(currentMinMax["min"], value)
            newMinMax["max"] = max(currentMinMax["max"], value)
        #finally we append the number into the stack
        self.minMaxStack.append(newMinMax)
        self.stack.append(value)

    # O(1) time , O(1) space
    def getMinValue(self): #returns the minimum number in stack
        return self.minMaxStack[len(self.minMaxStack) - 1]["min"]

    # O(1) time , O(1) space
    def getMaxValue(self): #returns the maximum number in stack
        return self.minMaxStack[len(self.minMaxStack) - 1]["max"]


# Input
obj = MinMaxStack()
print("Push 5, 8 and 3 into the stack")
obj.push(5)
obj.push(8)
obj.push(3)
print("Stack:", obj.stack)
print("minMaxStack:", obj.minMaxStack)
print("min:", obj.getMinValue())
print("max:", obj.getMaxValue())
print("\npop:", obj.pop())
print("Stack:", obj.stack)
print("minMaxStack:", obj.minMaxStack)
print("min:", obj.getMinValue())
print("max:", obj.getMaxValue())
print("\npop:", obj.pop())
print("Stack:", obj.stack)
print("minMaxStack:", obj.minMaxStack)
print("min:", obj.getMinValue())
print("max:", obj.getMaxValue())
