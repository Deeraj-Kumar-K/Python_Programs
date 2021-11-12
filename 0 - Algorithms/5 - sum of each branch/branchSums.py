# Branch Sums
# Return an array containing sum of each branch of a binary tree
'''
Binary Tree
       1
     /   \
    2     7
   / \
  3   9

Output: [6, 12, 8]
1st branch sum: 1+2+3 = 6
2nd branch sum: 1+2+9 = 12
3rd branch sum: 1+7 = 8
'''

# Time: O(n) , Space: O(n)
'''
O(n) time cause we visit 'n' nodes
O(n) space cause we return an array of size = no.of leaf nodes
no.of leaf nodes in binary tree = (n/2) approx. = O(n) space
Also if we have only one long branch then 'n' frames in call stack
'''

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def branchSums(root):
    sums = []
    calculateBranchSums(root, 0, sums)
    return sums

def calculateBranchSums(node, runningSum, array):
    if node is None:
        return
    currentSum = runningSum + node.value
    # if we reach leaf node, append sum to array
    if node.left is None and node.right is None:
        array.append(currentSum)
        return
    # if not a leaf node, recursively call child nodes
    calculateBranchSums(node.left, currentSum, array)
    calculateBranchSums(node.right, currentSum, array)


# Create root node
root = BinaryTree(1)

# Create child nodes of binary tree
b = BinaryTree(2)
c = BinaryTree(7)
d = BinaryTree(3)
e = BinaryTree(9)

# Connect child nodes to their parent nodes
root.left = b
root.right = c
b.left = d
b.right = e

# Display the output
result = branchSums(root)
print(result)
