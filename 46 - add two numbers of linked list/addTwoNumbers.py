# https://leetcode.com/problems/add-two-numbers/

# Add Two Numbers
#You are given two non-empty linked lists representing two non-negative integers
#The digits are stored in reverse order, and each of their nodes contains a single digit.
#Add the two numbers and return the sum as a linked list.
'''
Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        #create a dummy node
        dummy = ListNode()
        
        #create current pointer for dummy node
        cur = dummy
    
        #addition using elementary method
        #Ex: 8 + 7 = 15 so we get = val=5, carry=1
        
        carry = 0
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            #new digit
            val = val1 + val2 + carry
            carry = val // 10
            val = val % 10
            cur.next = ListNode(val)
            
            #update pointers
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        #here we return dummy node and not current node
        #cause current node is pointing to last node
        return dummy.next
        
            