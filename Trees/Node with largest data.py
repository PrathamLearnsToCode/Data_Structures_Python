class BinaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def Input():
    rootData = int(input())
    if rootData == -1:
        return None
    root = BinaryTreeNode(rootData)
    leftinput = Input()
    rightinput = Input()
    root.left = leftinput
    root.right = rightinput
    return root

def largestNumber(root):
    if root == None:
        return -1
    leftLargest = largestNumber(root.left)
    rightLargest = largestNumber(root.right)
    largest = max(leftLargest,rightLargest,root.data)
    return largest

root = Input()
print(largestNumber(root))