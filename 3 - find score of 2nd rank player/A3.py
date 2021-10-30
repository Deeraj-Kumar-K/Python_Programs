if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    #write your code here
    max1 = max(arr)
    big = -100 #constraints start from -100
    for item in arr:
            if big < item and item!=max1:
                big = item
    print(big)
