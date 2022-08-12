class BinarySearchTree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def Input():
    rootData = int(input())
    if rootData == -1:
        return None
    root = BinarySearchTree(rootData)
    root.left = Input()
    root.right = Input()
    return root

def printTreeDetailed(root):
    if root == None:
        return None
    print(root.data, end=":")
    if root.left != None:
        print("L",root.left.data,end = ",")
    if root.right != None:
        print("R",root.right.data)
    printTreeDetailed(root.left)
    printTreeDetailed(root.right)


def RemoveLeaves(root):
    if root == None:
        None
    if root.left == None and root.right == None:
        return None
    root.left = RemoveLeaves(root.left)
    root.right = RemoveLeaves(root.right)
    return root

root = Input()
print(printTreeDetailed(root))
root = RemoveLeaves(root)
print(printTreeDetailed(root))