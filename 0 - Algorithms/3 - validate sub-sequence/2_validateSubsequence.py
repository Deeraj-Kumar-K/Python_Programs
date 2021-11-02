# Subsequence is subset of a sequence
# we get by removing some elements from original sequence
# without changing order/positions of elements
# For Ex: Sequence=[1,2,3,4,5,6]
# then Subsequence=[1,3,6]
# NOT Subsequence=[6,4,5] because not in order

# Solution : Using for loop

# Time:O(n) , Space:O(1)

def validateSubSeq(arr,seq):
    #here arr is sequence , seq is subsequence
    seqIndex = 0
    for value in arr:
        if seqIndex == len(seq):
            break
        if seq[seqIndex] == value:
            seqIndex += 1

    return seqIndex == len(seq)


sequence = [1,2,3,4,5,6]
subSequence = [1,2,5,6]
print("Sequence = ",sequence,"\n")
print("Subsequence = ",subSequence)
print(validateSubSeq(sequence,subSequence))

subSequence = [6,1,5]
print("Subsequence = ",subSequence)
print(validateSubSeq(sequence,subSequence))
