class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class Queue:
    def __init__(self):
        self.rear=None
        self.front=None
        self.count=0

    def isEmpty(self):
        return self.count==0

    def enQueue(self,data):
        n=Node(data)
        if self.isEmpty():
            self.rear=self.front=n
            self.count=1
        else:
            self.rear.next=n
            self.rear=n
            self.count+=1
    def deQueue(self):
        if self.isEmpty():
            print("Queue underflow")
        elif self.front==self.rear:
            self.front=self.rear=None
            self.count=0
        else:
            self.front=self.front.next
            self.count-=1
    def size(self):
        return self.count

    def getFront(self):
        if self.isEmpty():
            return None
        return self.front.data

    def getRear(self):
        if self.isEmpty():
            return None
        return self.rear.data


# x=Queue()
# x.enQueue(1)
# x.enQueue(2)
# x.enQueue(3)
# x.enQueue(4)
# x.enQueue(5)
# x.enQueue(6)
# x.deQueue()
# x.deQueue()
# x.deQueue()
# x.deQueue()
# x.deQueue()
# x.deQueue()
# x.deQueue()
# x.enQueue(1)
# x.enQueue(2)
# print(f"size={x.size()}")
# # print(x.isEmpty())
# print(x.getFront())
# print(x.getRear())