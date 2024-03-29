class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def push(self,new_data):

        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def getNth(self,index):
        count = 0
        while self.head != None:
            if count == index:
                return self.head.data
            count = count + 1
            self.head = self.head.next

        return False


if __name__ == '__main__':
    llist = LinkedList()

    # Use push() to construct below list
    # 1->12->1->4->1
    llist.push(1)
    llist.push(4)
    llist.push(1)
    llist.push(12)
    llist.push(1)

    n = 3
    print("Element at index 3 is :", llist.getNth(n))

