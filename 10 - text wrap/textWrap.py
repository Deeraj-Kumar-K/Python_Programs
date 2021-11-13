# https://www.hackerrank.com/challenges/text-wrap/problem

# Text Wrap
# You are given a string and width w .
# Your task is to wrap the string into a paragraph of width w.
'''
Sample Input:
ABCDEFGHIJKLIMNOQRSTUVWXYZ
4

Sample Output:
ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ
'''

def wrap(string, max_width):
    newString = ''
    n=0
    while(n<len(string)):
        n1=n+max_width
        
        if(n1>len(string)):
            newString += string[n:]
            break
        
        newString += string[n:n1] + '\n'
        n=n+max_width
        
    return newString


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
