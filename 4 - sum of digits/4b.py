#https://www.codechef.com/problems/FLOW006
#Sum of digits

t=int(input())
arr = []
for i in range(t):
    num=input()
    arr.append(num)
sum=0
for n in arr:
    for digit in n:
        sum += int(digit)
    print(sum)
    sum = 0
