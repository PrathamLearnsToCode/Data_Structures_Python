class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def InsertAtI(head,i,data):
    prev = None
    curr = head
    count = 0
    while count<i:
        prev = curr
        curr = curr.next
        count = count + 1





def takeInput():
    inputList = [int(ele) for ele in input().split()]
    head = None
    tail = None
    for i in inputList:
        if i == -1:
            break
        newNode = Node(i)
        if head is None:
            head = newNode
            tail = newNode
        else:
            tail.next = newNode
            tail = newNode

    return head


