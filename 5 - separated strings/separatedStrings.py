# https://www.hackerrank.com/challenges/30-review-loop/problem

# print even-indexed and odd-indexed characters of given string
# as  2-space-separated strings on a single line
# Ex: Sring s=abaca
# Result: aaa bc


t = int(input("No. of test cases: ")) 
s=[]
for i in range(t):
    s.append(input("Enter String: "))
    
for item in s:
    length=len(item)
    
    for evenIdx in range(0,length,2):
        print(item[evenIdx],end="")
        
    print(" ",end="")
    
    for oddIdx in range(1,length,2):
        print(item[oddIdx],end="")
    print()
