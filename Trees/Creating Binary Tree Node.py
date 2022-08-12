class BinaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

bt1 = BinaryTreeNode(1)
bt2 = BinaryTreeNode(4)
bt3 = BinaryTreeNode(5)

bt1.left = bt2
bt1.right = bt3

