class BinaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def sumofNodes(root):
    if root == None:
        return 0
    rootData = root.data
    rootDataleft = sumofNodes(root.left)
    rootDataright = sumofNodes(root.right)
    return rootData + rootDataleft + rootDataright

def printTree(root):
    if root == None:
        return
    print(root.data,end = "->")
    if root.left != None:
        print("L:", root.left.data, end = ",")
    if root.right != None:
        print("R:", root.right.data, end = "")
    print()
    printTree(root.left)
    printTree(root.right)

bn1 = BinaryTreeNode(1)
bn2 = BinaryTreeNode(2)
bn3 = BinaryTreeNode(3)
bn4 = BinaryTreeNode(4)
bn5 = BinaryTreeNode(5)

bn1.left = bn2
bn1.right = bn3
bn2.left = bn4
bn2.right = bn5

print(sumofNodes(bn1))


