class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Inserting in Front
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Inserting in between
    def insertAfter(self,prev_node,new_data):
        if prev_node is None:
            print("The given previous node must in LinkedList.")
            return

        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    # Inserting in end
    def append(self,new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return

        while self.head.next is not None:
            self.head = self.head.next

        self.head.next = new_node

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data, "->", end=" ")
            temp = temp.next


# Code execution starts here
if __name__ == '__main__':
    # Start with the empty list
    llist = LinkedList()

    # Insert 6.  So linked list becomes 6->None
    llist.append(6)

    # Insert 7 at the beginning. So linked list becomes 7->6->None
    llist.push(7);

    # Insert 1 at the beginning. So linked list becomes 1->7->6->None
    llist.push(1);

    # Insert 4 at the end. So linked list becomes 1->7->6->4->None
    llist.append(4)

    # Insert 8, after 7. So linked list becomes 1 -> 7-> 8-> 6-> 4-> None
    llist.insertAfter(llist.head.next, 8)

    print('Created linked list is: ')
    llist.printList()

















