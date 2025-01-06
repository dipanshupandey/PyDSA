from singlyLinkedList import  *

class stack(sll):
    def __init__(self):
        super().__init__()
        self.top=None
        self.count=0

    def isempty(self):
        return super().isempty()
    def push(self,data):
        self.insertAtStart(data)
        self.count+=1

    def peek(self):
        if self.isempty():
            print("No Value Found")
            return
        return self.start.value
    def pop(self):
        if self.isempty():
            print("No Value Found")
            return
        self.deleteFirst()

        if self.count>0:
            self.count -= 1
    def size(self):
        print("size is ",self.count)
# st=stack()
# st.size()
# print(st.isempty())
# st.peek()
# st.push(1)
# st.push(2)
# st.push(3)
# st.push(4)
# st.push(5)
# st.size()
# print(st.peek())
# st.pop()
#
# st.pop()
#
# st.pop()
#
# st.pop()
# st.size()
# st.pop()
# st.size()
# st.pop()
# st.size()