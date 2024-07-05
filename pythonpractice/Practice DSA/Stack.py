class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None

class linkedlist:
    def __init__(self):
        self.head=None
        # self.tail=None
    
class Stack:
    def __init__(self):
        self.ll=linkedlist()
        
    def __str__(self):
        curr=self.ll.head
        op=[]
        while curr:
            op.append(str(curr.data))
            curr=curr.prev
        return '\n'.join(op)
    
    def append(self,data):
        node=Node(data)
        if not self.ll.head:
            self.ll.head=node
            # self.ll.tail=node
        else:
            node.prev=self.ll.head
            self.ll.head=node
        
    def is_empty(self):
        if self.ll.head is None:
            return True
        else:
            return False
    
    def pop(self):
        popped_node=self.ll.head
        
        if self.is_empty():
            return 'No data to pop'
        else:
            self.ll.head=None
            self.ll.head=popped_node.prev
        return popped_node.__dict__
            
s=Stack()
print(s.is_empty())
print(s.pop())
s.append(10)
s.append(11)
s.append(12)
s.append(13)
print(s.pop())
print(s.pop())
print(s.pop())
print(s.is_empty())
print(s)
        
        
        
        
        