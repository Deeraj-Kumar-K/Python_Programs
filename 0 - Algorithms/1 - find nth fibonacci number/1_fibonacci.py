# Find Nth Fibonacci number
# Using Recursion
# Time: O(2^n) , Space: O(n)

def fib(n):
    if n == 2:
        return 1
    elif n == 1:
        return 0
    else:
        return fib(n-1) + fib(n-2)


n = int(input("Enter a number: "))
print("Nth Fibonacci number is: ",fib(n))

# Fibonacci Series: 0 1 1 2 3 5 8.....
# For n=5 , ans=3
# For n=6 , ans=5
# For n=7, ans=8