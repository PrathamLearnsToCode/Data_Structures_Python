class LinkedList:
    def __init__(self,data):
        self.data = data
        self.next = None

a = LinkedList(13)
b = LinkedList(15)

a.next = b
print(b.next)