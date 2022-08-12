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
    print(root.data, end = ":")
    if root.left != None:
        print("L",root.left.data,end = ",")
    if root.right != None:
        print("R",root.right.data)
    printTreeDetailed(root.left)
    printTreeDetailed(root.right)

def height(root):
    if root==None:
        return 0
    return 1+max(height(root.left),height(root.right))

def isBalanced(root):
    if root == None:
        return True
    lt = height(root.left)
    rt = height(root.right)
    if lt-rt>1 or rt-lt>1:
        return False

    isleftBalanced = isBalanced(root.left)
    isrightBalanced = isBalanced(root.right)
    if isleftBalanced and isrightBalanced:
        return True
    else:
        return False



