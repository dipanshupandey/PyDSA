class PQ:
    def __init__(self):
        self.l=[]

    def isEmpty(self):
        return len(self.l) ==0


    def push(self,data=None):
        if self.isEmpty():
            self.l.append(data)
        else:
            i=0
            while i <len(self.l):
                if data < self.l[i]:
                    break
                i+=1
            self.l.insert(i,data)

    def traverse(self):
        if self.isEmpty():
            print("Noting to print")
        else:
            for x in self.l:
                print(x)

    def pop(self):
        if self.isEmpty():
            print("Noting to delete")
        else:
            self.l.pop(0)

    def size(self):
        return len(self.l)
x=PQ()

x.pop()
x.push(5)
x.push(4)
x.push(3)
print(x.size())
x.push(2)
x.pop()
x.push(6)
x.push(1)
x.pop()
x.pop()
x.pop()
x.pop()
x.pop()

x.traverse()
print(x.isEmpty())