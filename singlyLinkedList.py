class node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class sll:
    def __init__(self, start=None):
        self.start = start

    def isempty(self):
        return self.start == None

    def insertAtStart(self, data=None):
        temp = node(data, self.start)
        self.start = temp
        self.traverse()

    def insertAtLast(self, data=None):
        temp = node(data)
        if self.start is not None:
            n = self.start
            while n.next is not None:
                n = n.next
            n.next = temp
        else:
            self.start = temp
        self.traverse()

    def traverse(self):
        n = self.start
        while n != None:
            print(n.value, end=" ")
            n = n.next
        print()

    def search(self, data):
        temp = self.start
        while temp is not None:
            if temp.value is data:
                return temp
            temp = temp.next
        return None

    def insertAfter(self, val, data):

        temp = self.search(val)
        if temp is not None:
            n = node(data, temp.next)
            temp.next = n
        else:
            print("no Node found")
        self.traverse()

    def deleteFirst(self):
        if self.start is not None:
            print(self.start.value)
            self.start = self.start.next
        # self.traverse()
    def deleteLast(self):
        if self.start is not None:
            if self.start.next is None:
                print(self.start.value)
                self.start = None
            else:
                temp = self.start
                while temp.next.next is not None:
                    temp = temp.next
                print(temp.next.value)
                temp.next = None
        # self.traverse()

    def deleteItem(self, data):
        if self.start is None:
            pass
        elif self.start.value == data:
            print(self.start.value)
            self.start = self.start.next
        else:
            slow = self.start
            fast = self.start.next
            while fast is not None and fast.value is not data:
                fast = fast.next
                slow = slow.next
            if fast is None:
                print("not found")
            else:
                print(fast.value)
                slow.next = fast.next
        # self.traverse()

head = sll()

head.insertAtStart(1)
head.insertAtLast(3)
head.insertAfter(1, 2)
head.insertAfter(3, 4)
head.deleteFirst()
head.deleteLast()
head.deleteItem(1)