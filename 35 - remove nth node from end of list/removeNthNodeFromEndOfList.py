# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Remove Nth Node From End of List
#Given head of linked list, remove nth node from end of the list and return its head.
'''
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Input: head = [1], n = 1
Output: []

Input: head = [1,2], n = 1
Output: [1]
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # both left and right points to head
        left = right = head
        
        #shift right pointer n steps ahead
        for _ in range(n):
            right = right.next
        
        #if right pointer=null, Ex: 1->2 , n=2, then two loop iterations.
        #n=2 means we have to remove '1' and return '2' from the linkedlist
        #in 1st iteration, right will point to '2' then in next iteration,
        # right will point to NULL, i.e 1->2->[right]
        #so we return head.next i.e '2'
        if not right:
            return head.next
        
        #move both pointers forward together
        while right.next: # if right.next != None, then execute the loop
            left = left.next
            right = right.next
            
        #connect n-1 node to n+1 node
        left.next = left.next.next
        
        #return the modified linkedlist
        return head

