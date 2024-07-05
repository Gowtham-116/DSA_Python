class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class llst:
    def __init__(self):
        self.head=None
        self.tail=None
        
    def __iter__(self):
        curr=self.head
        while curr:
            yield curr.data
            curr=curr.next
class Queue:
    def __init__(self):
        self.ll=llst()
    
    def __str__(self):
        op=[str(i) for i in self.ll]
        return ' '.join(op)
    def enqueue(self,data):
        new_node=Node(data)
        if self.ll.head is None:
            self.ll.head=new_node
            self.ll.tail=new_node
        
        else:
            self.ll.tail.next=new_node
            self.ll.tail=new_node
        
    def is_empty(self):
        if self.ll.head:
            return False
        else:
            return True
            
            
    def dequeue(self):                    
        tempNode = self.ll.head
        if self.ll.head == self.ll.tail:
            self.ll.head = None
            self.ll.tail = None
        else:
            self.ll.head = self.ll.head.next
        return tempNode
    
    def pop(self):
        if self.ll.head==self.ll.tail:
            self.ll.head= None
            self.ll.tail=None
        else:
            curr=self.ll.head
            while curr:
                if curr.next == self.ll.tail:
                    self.ll.tail=curr
                    self.ll.tail.next=None
                curr=curr.next
                # curr=curr.next
            return curr
    
    def len(self):
        curr=self.ll.head
        lt=0
        while curr:
            lt+=1
            curr=curr.next
        return lt
        
q=Queue()
q.enqueue(10)
q.enqueue(110)
q.enqueue(101)
print(q.dequeue().__dict__)
print(q.len())
# print(q)
# q.pop()
# print(q.len())
# print(q.is_empty())
print('_'*20)
print(q)
print('_'*20)
