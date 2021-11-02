# Subsequence is subset of a sequence
# we get by removing some elements from original sequence
# without changing order/positions of elements
# For Ex: Sequence=[1,2,3,4,5,6]
# then Subsequence=[1,3,6]
# NOT Subsequence=[6,4,5] because not in order

# Solution : Using while loop

# Time:O(n) , Space:O(1)

def validateSubSeq(arr,seq):
    #here arr is sequence , seq is subsequence
    arrIndex = 0
    seqIndex = 0
    while arrIndex < len(arr) and seqIndex < len(seq):
        if seq[seqIndex] == arr[arrIndex]:
            seqIndex += 1

        arrIndex += 1
    #this returns true if all elements have been traversed
    return seqIndex == len(seq)


sequence = [1,2,3,4,5,6]
subSequence = [1,3,6]
print("Sequence = ",sequence,"\n")
print("Subsequence = ",subSequence)
print(validateSubSeq(sequence,subSequence))

subSequence = [6,4,5]
print("Subsequence = ",subSequence)
print(validateSubSeq(sequence,subSequence))
