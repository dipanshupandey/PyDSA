from singlyLinkedList import  *

class stack:
    def __init__(self):
        self.sl=sll()

    def isEmpty(self):
        return self.sl.isempty()

    def push(self,data=None):
        self.sl.insertAtLast(data)

    def pop(self):
        if self.sl.isempty()==False:
            self.sl.deleteLast()
        else:
            print("Empty List")

    def peek(self):
        if self.sl.isempty() == False:
            print(self.sl.start.value)
        else:
            print("No Item Found")

# st=stack()
# st.push(1)
# st.push(2)
# st.push(3)
# st.peek()
# st.push(4)
# st.pop()
# st.pop()
# st.pop()
# st.pop()
# st.pop()
# st.pop()
# st.pop()