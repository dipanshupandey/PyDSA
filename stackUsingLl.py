class node:
    def __init__ (self,data=None,next=None):
        self.data=data
        self.next=next

class stackk:
    def __init__(self,top=None):
        self.top=None
        self.no=0


    def isEmpty(self):
        return self.top == None

    def push(self,data=None):
        temp=node(data,self.top)
        self.top=temp
        self.no+=1

    def pop(self):
        if self.isEmpty():
            raise IndexError("Stack Is Empty")
        else:
            print(self.top.data," Deleted")
            self.top=self.top.next
        if self.no != 0:
            self.no-=1

    def peek(self):
        if self.isEmpty():
            raise IndexError("No element found")
        else:
            print(self.top.data)

    def count(self):

        return self.no
st=stackk()

print(st.isEmpty())

st.push((1))
st.push((2))
st.push((3))
print("Number of elements",st.no)
st.peek()
st.push((4))
st.pop()
st.pop()
st.pop()
st.pop()
# st.pop()
st.push(5)
st.pop()
print("Number of elements",st.no)