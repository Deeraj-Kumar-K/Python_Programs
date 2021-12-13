# Find Closest Value in Binary Search Tree
'''
       10
      /  \
    5     15
   / \    / \
  2   5  13  22
 /        \
1         14

Input = 12, Output = 13
'''

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.val)
#*********************************************************************
'''
# Solution - 1 : Using Recursion
# Avg: O(log(n)) time , O(log(n)) space
# Worst: O(n) time , O(n) space

def findClosestValueInBST(tree, target):
    return findClosestValueInBstHelper(tree, target, float('inf'))

def findClosestValueInBstHelper(node, target, closest):
    if node is None:
        return closest

    if abs(target - closest) > abs(target - node.val):
        closest = node.val

    if target < node.val:
        return findClosestValueInBstHelper(node.left, target, closest)
    elif target > node.val:
        return findClosestValueInBstHelper(node.right, target, closest)
    else:
        return closest
'''    


# Solution - 2 : Using Iteration
# Avg: O(log(n)) time , O(1) space
# Worst: O(n) time , O(1) space

def findClosestValueInBST(tree, target):
    return findClosestValueInBstHelper(tree, target, float('inf'))

def findClosestValueInBstHelper(tree, target, closest):
    node = tree
    while node != None:
        if abs(target - closest) > abs(target - node.val):
            closest = node.val

        if target > node.val:
            node = node.right
        elif target < node.val:
            node = node.left
        else:
            break
    return closest


#*********************************************************************
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)

root.left.left = TreeNode(2)
root.left.right = TreeNode(5)
root.left.left.left = TreeNode(1)

root.right.left = TreeNode(13)
root.right.right = TreeNode(22)
root.right.left.right = TreeNode(14)

result = findClosestValueInBST(root, 12)
print(result)
