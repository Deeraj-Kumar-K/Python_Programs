# Node Depths
# Return sum of depth of all nodes in binary tree.
'''
Following binary tree is showing value of depth of each node.
       0
     /   \
    1     1
   / \    / \
  2   2  2   2
 / \     
3   3         

Explanation:
Root node's depth value = 0 and its child's depth value = +1 and so on.
So for above example we get, 0+1+1+2+2+2+2+3+3 = 16
Output = 16
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
# Solution - 1 : Using Stack (Iterative)
# O(n) time , O(h) space
# where n is no. of nodes, h is height of tree

def nodeDepths(root):
    sumOfDepths = 0
    stack = [
                {
                "node": root,
                "depth": 0
                }
            ]

    while len(stack) > 0:
        nodeInfo = stack.pop()
        node = nodeInfo["node"]
        depth = nodeInfo["depth"]

        if node is None:
            continue

        sumOfDepths += depth

        stack.append({"node": node.left, "depth": depth + 1})
        stack.append({"node": node.right, "depth": depth + 1})
        
    return sumOfDepths
    '''   


# Solution - 2 : Using Recursion
# O(n) time , O(h) space

def nodeDepths(root, depth = 0):
    #handling base case of recursion
    if root is None:
        return 0
    return depth + nodeDepths(root.left, depth+1) + nodeDepths(root.right, depth+1)


#*********************************************************************
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

root.left.left.left = TreeNode(8)
root.left.left.right = TreeNode(9)

result = nodeDepths(root)
print(result)
