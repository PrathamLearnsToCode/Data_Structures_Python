import queue
class BinarySearchTree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def search(root,x):
    if root == None:
        return False
    if root.data == x:
        return True
    elif root.data>x:
        return search(root.left,x)
    elif root.data<x:
        return search(root.right,x)

def printTreeDetailed(root):
    if root == None:
        return None
    print(root.data,end = ":")
    if root.left != None:
        print("L",root.left.data,end = ",")
    if root.right != None:
        print("R",root.right.data)
        printTreeDetailed(root.left)
        printTreeDetailed(root.right)

def LevelWiseInput():
    q = queue.Queue()
    print("Enter root")
    rootData = int(input())
    if rootData == -1:
        return None
    root = BinarySearchTree(rootData)
    q.put(root)
    while(not(q.empty())):
        currentData = q.get()
        print("Enter left child of:",currentData.data)
        leftChildData = int(input())
        if leftChildData != -1:
            leftChild = BinarySearchTree(leftChildData)
            currentData.left = leftChild
            q.put(leftChild)

        print("Enter right child of:", currentData.data)
        rightChildData = int(input())
        if rightChildData != -1:
            rightChild = BinarySearchTree(rightChildData)
            currentData.right = rightChild
            q.put(rightChild)

    return root

root = LevelWiseInput()
printTreeDetailed(root)
print(search(root,9))
