class QueueusingArray:
    def __init__(self):
        self.__arr = []
        self.__count = 0
        self.__front = 0

    def enQueue(self,data):
        self.__arr.append(data)
        self.__count += 1

    def deQueue(self):
        if self.__count == 0:
            return -1
        element = self.__arr[self.__front]
        self.__front += 1
        self.__count -= 1
        return element
    def front(self):
        if self.__count == 0:
            return -1
        return self.__arr[self.__front]

    def size(self):
        return self.__count

    def isEmpty(self):
        return self.size() == 0

q = QueueusingArray()
q.enQueue(1)
q.enQueue(2)
q.enQueue(3)
q.enQueue(4)
q.enQueue(5)

while (q.isEmpty() is False):
    print(q.front())
    q.deQueue()

print(q.deQueue())

