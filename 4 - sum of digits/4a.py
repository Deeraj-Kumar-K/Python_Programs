#https://www.codechef.com/problems/FLOW006
#Sum of digits

t=int(input())
arr = []
for i in range(t):
    num=int(input())
    arr.append(num)
sum=0
for n in arr:
    while(n>0):
        rem = n%10
        sum += rem
        n = n//10
    print(sum)
    sum = 0
