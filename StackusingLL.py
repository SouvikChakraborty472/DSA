class node:

    def __init__(self,value):
        self.data = value
        self.next = None

class Stack:

    def __init__(self):
        self.top = None

    def isempty(self):
        return self.top == None
        
    def push(self,value):
        new_node = node(value)
        new_node.next = self.top
        self.top = new_node

    def traverse(self):
        tep = self.top
        while tep != None:
            print(tep.data)
            tep = tep.next

    def peek(self):
        if (self.isempty()):
            return 'Stack Empty'
        else:
            return self.top.data
        
    def pop(self):
        if(self.isempty()):
            return 'stack Empty'
        else:
            self.top = self.top.next

s = Stack()
s.push(2)
s.push(3)
s.push(4)
s.push(5)
s.traverse()

s.pop()
print(s.peek())