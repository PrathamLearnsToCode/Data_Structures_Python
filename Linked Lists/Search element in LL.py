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

    def search(self,key):
        while self.head != None:
            if self.head.data == key:
                return True
            self.head = self.head.next

        return False


if __name__ == '__main__':

    # Start with the empty list
    llist = LinkedList()
    llist.push(10)
    llist.push(30)
    llist.push(11)
    llist.push(21)
    llist.push(14)

    # Function call
    if llist.search(15):
        print("Yes")
    else:
        print("No")

