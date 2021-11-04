# Find three largest numbers in the array
# Ex: [-1,2,3,4,5,6] Ans=[4,5,6]

#Time:O(n) , Space:O(1)

# function to calculate three largest numbers
def findThreeLargestNum(array):
    threeLargest=[None, None, None]
    for num in array:
        findPosition(num,threeLargest)
    return threeLargest

# helper function to update threeLargest array
def findPosition(num, threeLargest):
    if threeLargest[2] is None or threeLargest[2] < num:
        shiftAndUpdate(num,threeLargest,2)
    elif threeLargest[1] is None or threeLargest[1] < num:
        shiftAndUpdate(num,threeLargest,1)
    elif threeLargest[0] is None or threeLargest[0] < num:
        shiftAndUpdate(num,threeLargest,0)

# to insert number inside threeLargest array
def shiftAndUpdate(num,array,index):
    for i in range(index+1):
        if i==index:
            array[i]=num
        else:
            array[i]=array[i+1]


array=[1,2,-2,-54,-4,20,100,50]
result=findThreeLargestNum(array)
print(array)
print("Three Largest Numbers:",result)
