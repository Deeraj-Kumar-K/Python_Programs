# https://www.hackerrank.com/challenges/collections-counter/problem

# Shoe shop, his shop has x number of shoes
# He has a list containing the size of each shoe he has in his shop.
# N number of customers are willing to pay y amount of money
# only if they get the shoe of their desired size.
# Compute how much money shop owner earned.
'''
Sample Input:
10
2 3 4 5 6 8 7 6 5 18
6
6 55
6 45
6 55
4 40
18 60
10 50

Sample Output:
200
'''

# Solution:
from collections import Counter

shoes = int(input())
sizes = list(map(int, input().split()))
counts = Counter(sizes)
customers = int(input())
need = []
for i in range(customers):
    temp = input().split()
    need.append(temp)
money = 0
for person in need:
    if int(person[0]) in counts:
        if counts[int(person[0])]!=0:
            counts[int(person[0])] -= 1
            money += int(person[1])
print(money)
