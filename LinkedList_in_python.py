class Node:
    def __init__(self, value):
        #creating data and next variable
        self.data = value
        self.next = None

class linkedlist:
    def __init__(self):
        #Empty linkedlist
        self.head = None
        self.n = 0

    def __len__(self):
        return self.n
    
    def insert_head(self, value):
        #new node
        new_node = Node(value)
        #create connection
        new_node.next = self.head
        self.head = new_node
        #increment n
        self.n += 1

    def __str__(self):
        curr = self.head
        result = ''
        while curr != None:
            result = result + str(curr.data) + '->'
            curr = curr.next

        return result[:-2]
    
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.hesd = new_node
            self.n += 1
            return
        
        curr = self.head
        while curr.next != None:
            curr = curr.next

        curr.next = new_node
        self.n += 1

    def insert_after(self,after,value):
        new_node = Node(value)
        curr = self.head
        while curr != None:
            if curr.data == after:
                break
            curr = curr.next
        
        if curr != None:
            new_node.next = curr.next
            curr.next = new_node
            self.n += 1
        else:
            return 'Item not found'
        
    def clear(self):
        self.head = None
        self.n = 0

    def delete_head(self):
        if self.head == None:
            return 'Empty LinkedList'
        self.head = self.head.next
        self.n -= 1

    def pop(self):
        if self.head == None:
            return 'Empty LinkedList'
        curr = self.head
        if self.n == 1:
            return self.delete_head()
        while curr.next.next != None:
            curr = curr.next
        curr.next = None
        self.n -= 1

    def remove(self,value):
        if self.head == None:
            return 'Empty LinkedList'

        if self.head.data == value:
            return self.delete_head()
        
        curr = self.head
        while curr.next != None:
            if curr.next.data == value:
                break
            curr = curr.next

        if curr.next == None:
            return 'not found'
        else:
            curr.next = curr.next.next

    def search(self,item):
        curr = self.head
        pos = 0
        while curr != None:
            if curr.data == item:
                return pos
            curr = curr.next
            pos += 1
        return 'item not found'
    
    def __getitem__(self,index):
        curr = self.head
        pos = 0
        while curr != None:
            if pos == index:
                return curr.data
            curr = curr.next
            pos += 1

        return 'IndexError'

L = linkedlist()
L.insert_head(1) 
L.insert_head(2)
L.insert_head(3)
L.insert_head(4)
print(L)
L.remove()
print(L)