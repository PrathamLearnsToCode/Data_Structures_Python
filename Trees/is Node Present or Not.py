class BinaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def isNodePresent(root,key):
    if root == None:
        return False
    if root.data == key:
        return True
    res1 = isNodePresent(root.left,key)
    if res1 == True:
        return True
    res2 = isNodePresent(root.right,key)
    if res2 == True:
        return True



bn1 = BinaryTreeNode(1)
bn2 = BinaryTreeNode(2)
bn3 = BinaryTreeNode(3)
bn4 = BinaryTreeNode(4)
bn5 = BinaryTreeNode(5)

bn1.left = bn2
bn1.right = bn3
bn2.left = bn4
bn2.right = bn5

if (isNodePresent(bn1, 7)):
    print("YES")
else:
    print("NO")


