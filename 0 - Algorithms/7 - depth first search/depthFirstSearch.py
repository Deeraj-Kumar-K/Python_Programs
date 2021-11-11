# Depth First Search (DFS)
# Go into depth of a branch traversing all the child

# Time: O(v+e) , Space: O(v)
# where v is no.of vertices, e is no.of edges

# Time is O(v+e) cause we traverse all vertices 'v' and
# we call DFS algo for each child, i.e 'e' edges

# Space is O(v) cause finally we return array of size 'v'
# and in worst case, we might get a tree having only one large branch
# so going into its depth, we get O(v) frames on call stack

class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(name)
        
    def depthFirstSearch(self, array=[]):
        # array stores all the nodes traversed/visited
        array.append(self.name)
        # for each child, call DFS algorithm
        for child in self.children:
            child.depthFirstSearch(array)
        return array


# Creating nodes/vertices
a = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")
e = Node("E")
f = Node("F")
g = Node("G")
h = Node("H")
i = Node("I")
j = Node("J")
k = Node("K")
#Adding child to parent nodes
a.addChild(b)
a.addChild(c)
a.addChild(d)
b.addChild(e)
b.addChild(f)
f.addChild(i)
f.addChild(j)
d.addChild(g)
d.addChild(h)
g.addChild(k)
# Print the output after traversal
print(a.depthFirstSearch())
#Output: ['A', 'B', 'E', 'F', 'I', 'J', 'C', 'D', 'G', 'K', 'H']
