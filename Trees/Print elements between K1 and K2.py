import queue
class BinarySearchTree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


def BetweenK1andK2(root,K1,K2):
    if root == None:
        return
    if root.data>K2:
        return BetweenK1andK2(root.left,K1,K2)
    elif root.data<K1:
        return BetweenK1andK2(root.right, K1, K2)
    else:
        print(root.data)
        BetweenK1andK2(root.left, K1, K2)
        BetweenK1andK2(root.right , K1, K2)

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
        current_node = q.get()
        print("Enter left root of",current_node.data)
        leftChildData = int(input())
        if leftChildData != -1:
            leftroot = BinarySearchTree(leftChildData)
            current_node.left = leftroot
            q.put(leftroot)

        print("Enter right child of:", current_node.data)
        rightChildData = int(input())
        if rightChildData != -1:
            rightChild = BinarySearchTree(rightChildData)
            current_node.right = rightChild
            q.put(rightChild)

    return root




