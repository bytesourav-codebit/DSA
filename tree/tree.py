import sys

# Node Structure for tree
class Node:
    def __init__ (self, x):
        self.data = x
        self.children = []

# Function to add a child to a node
def addChild (parent, child):
    parent.children.append(child)

# Function to print parent of each node
def printParents (node, parent):
    if parent is None:
        print(str(node.data) + " -> NULL ")
    else:
        print(str(node.data) + " -> " + str(parent.data))

    for child in node.children:
        printParents(child, node)

# Function to print children of each node
def printChildren (node):
    children_str = " ".join(str(child.data) for child in node.children)
    print(str(node.data) + " -> " + children_str)

    for child in node.children:
        printChildren(child)

# Function to print leaf nodes
def printLeafNodes (node):
    if not node.children:
        sys.stdout.write(str(node.data) + " ")
        return
    
    for child in node.children:
        printLeafNodes(child)

# Function to print degree of each node
def printDegrees (node, parent):
    degree = len(node.children)
    if parent is not None:
        degree += 1
    print(str(node.data) + " -> " + str(degree))

    for child in node.children:
        printDegrees(child, node)

# Main execution
if __name__ == "__main__":
    # Creating Nodes
    root = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    
    # Constructing tree
    addChild(root, n2)
    addChild(root, n3)
    addChild(n2, n4)
    addChild(n2, n5)

    print("Parents of each node: ")
    printParents(root, None)

    print("Children of each node: ")
    printChildren(root)

    print("Leaf nodes: ")
    printLeafNodes(root)
    print("\n")

    print("Degree of nodes: ")
    printDegrees(root, None)