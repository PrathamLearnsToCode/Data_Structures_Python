class BinaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def printTreeDetailed(root):
    if root == None:
        return
    print(root.data,end = ":")
    if root.left != None:
        print("L", root.left.data, end = ",")
    if root.right != None:
        print("R",root.right.data)
    printTreeDetailed(root.left)
    printTreeDetailed(root.right)

def Input():
    rootData = int(input())
    if rootData == -1:
        return None
    root = BinaryTreeNode(rootData)
    leftTree = Input()
    rightTree = Input()
    root.left = leftTree
    root.right = rightTree
    return root

bt5 = BinaryTreeNode(5)
bt4 = BinaryTreeNode(4)
bt3 = BinaryTreeNode(3)
bt2 = BinaryTreeNode(2)
bt1 = BinaryTreeNode(1)

bt5.left = bt4
bt5.right = bt3
bt4.left = bt2
bt4.right = bt1
root = Input()
print(printTreeDetailed(root))


