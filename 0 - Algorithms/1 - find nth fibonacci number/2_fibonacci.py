# Find Nth Fibonacci number
# Fibonacci Series: 0 1 1 2 3 5 8.....n
# Using Hash table
# Time: O(n) , Space: O(n)

def fib(n, hashTable={1:0,2:1}):
    if n in hashTable:
        return hashTable[n]
    else:
        hashTable[n] = fib(n-1, hashTable) + fib(n-2, hashTable)
        return hashTable[n]


n = int(input("Enter a number: "))
print("Nth Fibonacci number is: ",fib(n))

# Fibonacci Series: 0 1 1 2 3 5 8.....
# For n=5 , ans=3
# For n=6 , ans=5
# For n=7, ans=8