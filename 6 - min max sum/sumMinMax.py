# Mini-Max Sum
# Given five positive integers, find the minimum and maximum values,
# that can be calculated by summing exactly four of the five integers
# Ex: arr=[1,2,3,4,5]
# Minimum sum is 1+2+3+4 = 10
# Max sum is 2+3+4+5 = 14
# Output: 10 14

def miniMaxSum(arr):
    minValue = min(arr)
    maxValue = max(arr)
    print(sum(arr)-maxValue,end=" ")
    print(sum(arr)-minValue)


if __name__ == '__main__':
    #arr = list(map(int, input().rstrip().split()))
    #Input: 1 2 3 4 5
    arr = [1, 2, 3, 4, 5]
    print(arr)
    miniMaxSum(arr)
