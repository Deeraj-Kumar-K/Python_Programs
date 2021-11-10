# https://www.hackerrank.com/challenges/30-2d-arrays/problem

# Given a 6x6 2D Array,
# Calculate the hourglass sum for every hourglass
# then print the maximum hourglass sum
'''
Hourglass is a subset of values with indices falling in this pattern
a b c
  d
e f g
There are 16 hourglasses, hourglass sum is the sum of an hourglass' values.

Run the program and copy-paste the input
Sample Input
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0

Sample Output
19
'''

# Solution:

if __name__ == '__main__':

    a = []
    for _ in range(6):
        a.append(list(map(int, input().rstrip().split())))

    
    large = -63
    s = 0
    for i in range(4):
        for j in range(4):
            s=a[i][j]+a[i][j+1]+a[i][j+2]+a[i+1][j+1]+a[i+2][j]+a[i+2][j+1]+a[i+2][j+2]
            if s>large:
                large=s
    print(large)


'''
The hourglass with the maximum sum (19) is:
2 4 4
  2
1 2 4
'''
