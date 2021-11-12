# # https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem

# Breaking the Records
#Given the scores, determine the no. of times player breaks his records
# for most and least points scored during the season.
'''
Input:
9
10 5 20 20 4 5 2 25 1

Output:
2 4
'''

def breakingRecords(scores):
    hl=[0,0]
    high,low = scores[0],scores[0]
    for score in scores:
        if score < low:
            hl[1]+=1
            low=score
        elif score > high:
            hl[0]+=1
            high=score
    return hl

if __name__ == '__main__':
    n = int(input())
    scores = list(map(int, input().rstrip().split()))
    result = breakingRecords(scores)
    print(result)
