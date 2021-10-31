# Find Nth Fibonacci number
# Using Iterative method
# Time: O(n) , Space: O(1)

def fib(n):
    lastTwo = [0,1]
    counter = 3
    while n>=counter:
        nextFib = lastTwo[0] + lastTwo[1]
        lastTwo[0] = lastTwo[1]
        lastTwo[1] = nextFib
        counter += 1
    return lastTwo[1] if n>1 else lastTwo[0]


n = int(input("Enter a number: "))
print("Nth Fibonacci number is: ", fib(n))

# Fibonacci Series: 0 1 1 2 3 5 8.....
# For n=5 , ans=3
# For n=6 , ans=5
# For n=7, ans=8
