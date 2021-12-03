# https://leetcode.com/problems/middle-of-the-linked-list/

# Middle of the Linked List
#Given head of a singly linked list, return the middle node of linked list.
#If there are two middle nodes, return the second middle node.
'''
Example 1:
Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.

Example 2:
Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4,
we return the second one.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # to count no.of nodes in linked list
    def getCount(self, node):
        count = 0
        while node:
            count +=1
            node=node.next
        return count
    
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = self.getCount(head) #contains no.of nodes
        count = count//2 + 1
        #count now contains middle node number
        
        result = ListNode()
        result = head
        #loop starts from i=0, so we take range till (count-1)
        for i in range(count - 1):
            result = result.next
        #now result contains address of middle node
        return result

