# Balanced Brackets

# Check if brackets (), [], {} are balanced or not.
# No. of opening brackets = No. of closing brackets
# Every opening bracket should correctly match with their closing bracket.
'''
Examples:
[ ] - true
[ } ] - false
( ( () {} ) [] ) - true
( ( ] - false
'''

# Time: O(n) , Space: O(n)
#We need O(n) memory because we are suing stack which can store n items.
#Ex: If we have input = {{{{{{, here O(n) items are stored
#Also if input = ((())), then memory = n/2 which is O(n) space

def balancedBrackets(string):
    
    openingBrackets = "[{("
    closingBrackets = "]})"

    #for every closing brackets, we have matching opening brackets
    matchingBrackets = { ')':'(' , ']':'[' , '}':'{' }

    stack = []

    for val in string:
        if val in openingBrackets:
            stack.append(val)
        elif val in closingBrackets:
            if len(stack) == 0:
                return False
            #if last item in stack is a matching opening bracket
            if stack[-1] == matchingBrackets[val]:
                stack.pop()
            else:
                return False
    #if stack is empty, then return true
    return len(stack) == 0


s = "(([][]()){})"
print(s)
print(balancedBrackets(s))

s = "[[["
print(s)
print(balancedBrackets(s))

