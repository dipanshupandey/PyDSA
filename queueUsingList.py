class Queue:
    def __init__(self):
        self.q=[]

    def isEmpty(self):
        return len(self.q) ==0

    def enQueue(self,data):
        self.q.append(data)

    def deQueue(self):
        if self.isEmpty():
            print("Queue is empty!")
            return
        print(f"{self.q[0]} deleted")
        self.q.pop(0)

    def getFront(self):
        if self.isEmpty():
            print("Queue is empty!")
        else:
            return self.q[0]

    def getRare(self):
        if self.isEmpty():
            print("Queue is empty!")
            return
        return self.q[-1]

    def size(self):
        if self.isEmpty():

            return 0

        else:

            return len(self.q)

# x=Queue()
# print(x.isEmpty())
# print(f"size is {x.size()}")
# x.enQueue(1)
# x.enQueue(2)
# x.enQueue(3)
# print(f"size is {x.size()}")
# x.enQueue(4)
# x.enQueue(5)
# x.enQueue(6)
# print(f"size is {x.size()}")
# x.deQueue()
# x.deQueue()
# x.deQueue()
# x.deQueue()
# x.deQueue()
# x.deQueue()
# x.deQueue()
# print(f"size is {x.size()}")
#
# print(x.getFront())
# print(x.getRare())