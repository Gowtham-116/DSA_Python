# # class Node:
# #     def __init__(self, value):
# #         self.value = value
# #         self.next = None

# # class LinkedList:
# #     # def __init__(self, value):
# #     #     new_node = Node(value)
# #     #     self.head = new_node
# #     #     self.tail = new_node
# #     #     self.length = 1
    
# #     def __init__(self):
# #         self.head = None
# #         self.tail = None
# #         self.length = 0
    
# #     def __str__(self):
# #         temp_node = self.head
# #         result = ''
# #         while temp_node is not None:
# #             result += str(temp_node.value)
# #             if temp_node.next is not None:
# #                 result += ' -> '
# #             temp_node = temp_node.next
# #         return result
    
# #     def append(self, value):
# #         new_node = Node(value)
# #         if self.head is None:
# #             self.head = new_node
# #             self.tail = new_node
# #         else:
# #             self.tail.next = new_node
# #             self.tail = new_node
# #         self.length += 1
    
# #     def prepend(self, value):
# #         new_node = Node(value)
# #         if self.head is None:
# #             self.head = new_node
# #             self.tail = new_node
# #         else:
# #             new_node.next = self.head
# #             self.head = new_node
# #         self.length += 1
    
# #     def insert(self, index, value):
# #         new_node = Node(value)
# #         if self.head is None:
# #             self.head = new_node
# #             self.tail = new_node
# #         elif index == 0:
# #             new_node.next = self.head
# #             self.head = new_node
# #         else:
# #             temp_node = self.head
# #             for _ in range(index-1):
# #                 temp_node = temp_node.next
# #             new_node.next = temp_node.next
# #             temp_node.next = new_node
# #         self.length += 1
    
# #     def traverse(self):
# #         current = self.head
# #         while current is not None:
# #             print(current.value)
# #             current = current.next
    
# #     def search(self, target):
# #         current = self.head
# #         while current is not None:
# #             if current.value == target:
# #                 return True
# #             current = current.next
# #         return False
    
# #     def search(self, target):
# #         current = self.head
# #         index = 0
# #         while current is not None:
# #             if current.value == target:
# #                 return index
# #             current = current.next
# #             index += 1
# #         return -1
    
# #     def get(self, index):
# #         if index == -1:
# #             return self.tail
# #         elif index < -1 or index >= self.length:
# #             return None
# #         current = self.head
# #         for _ in range(index):
# #             current = current.next
# #         return current
    
# #     def set_value(self, index, value):
# #         temp = self.get(index)
# #         if temp:
# #             temp.value = value
# #             return True
# #         return False
    
# #     def pop_first(self):
# #         if self.length == 0:
# #             return None
# #         popped_node = self.head
# #         if self.length == 1:
# #             self.head = None
# #             self.tail = None
# #         else:
# #             self.head = self.head.next
# #             popped_node.next = None
# #         self.length -= 1
# #         return popped_node
    
    
    
# #     def pop(self):
# #         if self.length == 0:
# #             return None
# #         popped_node = self.tail
# #         if self.length == 1:
# #             self.head = self.tail = None
# #         else:
# #             temp = self.head
# #             while temp.next is not self.tail:
# #                 temp = temp.next
# #             temp.next = None
# #             self.tail = temp
# #         self.length -= 1
# #         return popped_node
    

# #     def remove(self, index):
# #         if index < -1 or index >= self.length:
# #             return None
# #         if index == 0:
# #             return self.pop_first()
# #         if index == -1 or index == self.length-1:
# #             return self.pop()
# #         prev_node = self.get(index-1)
# #         popped_node = prev_node.next
# #         prev_node.next = popped_node.next
# #         popped_node.next = None
# #         self.length -= 1
# #         return popped_node
    

# #     # def remove(self, index):
# #     #     prev_node = self.get(index-1)
# #     #     popped_node = prev_node.next
# #     #     prev_node.next = popped_node.next
# #     #     popped_node.next = None
# #     #     self.length -= 1
# #     #     return popped_node




# # linked_list = LinkedList()
# # linked_list.append(10)
# # linked_list.append(20)
# # linked_list.append(30)
# # linked_list.append(40)
# # linked_list.prepend(100)
# # print(linked_list)
# # print(linked_list.remove(0))
# # print(linked_list)


# #-----------------------------CIRCULAR SINGLY LINKED LIST------------------------
# # class Node:
# #     def __init__(self,value):
# #         self.value=value
# #         self.next=None

# # class CSLL:
# #     def __init__(self):
# #         self.head=None
# #         self.tail=None
# #         self.length=0
        
# #     def __str__(self) -> str:
# #         curr=self.head
# #         # print('curr',curr)
# #         csl=[]
# #         while curr:
# #             csl.append(curr.value)
# #             curr=curr.next
# #             # print(str(csl))
# #             if curr==self.head:
# #                 return str(csl)
# #             #     print(str(csl))
# #         return str(csl)
      
# #     def append(self,value):
# #         new_node=Node(value)
# #         # new_node.next=new_node
# #         if self.head==None:
# #             self.head=new_node
# #             self.tail=new_node
# #             self.tail.next=self.head  #new_node.next=new_node
# #             self.length=1
# #         else:
# #             self.tail.next=new_node
# #             self.tail=new_node
# #             self.tail.next=self.head #new_node.next=new_node
# #             self.length+=1
# #         # print(f'{self.head}\n{self.head.next}\n{self.tail}\n{self.tail.next}-')
            
# #     def prepend(self,value):
# #         new_node=Node(value)
# #         if self.head==None:
# #             self.head=new_node
# #             self.tail=new_node
# #             self.tail.next=new_node
# #         else:
# #             # curr=self.head
# #             new_node.next=self.head
# #             self.head=new_node
# #             self.tail.next=new_node
# #         self.length+=1
# #         # print(f'{self.head}\n{self.head.next.__dict__}\n{self.tail.__dict__}\n{self.tail.next.__dict__}-')
        
# #     def insert(self,idx,value):
# #         new_node=Node(value)
# #         if self.head is None:
# #             self.head=new_node
# #             self.tail=new_node
# #             self.tail.next=new_node
# #             self.length+=1
# #         else:
# #             curr=self.head
# #             if idx==0:
# #                 new_node.next=curr
# #                 self.head=new_node
# #                 self.tail.next=self.head
# #                 self.length+=1
# #             else:
# #                 while curr:
# #                     if idx>=1 and idx<self.length:
# #                         new_node.next=curr.next
# #                         curr.next=new_node
# #                         self.length+=1
# #                         break
# #                     if idx>self.length or idx<0:
# #                         try:
# #                             # idx=0
# #                             new_node.next=curr
# #                             self.head=new_node
# #                             self.tail.next=self.head
# #                             self.length+=1
# #                             # return None
# #                         except:
# #                             Exception('index out of range')
# #                         break
# #                     curr=curr.next
# #         # print(f'{self.head}\n{self.head.next.__dict__}\n{self.tail.__dict__}\n{self.tail.next.__dict__}*')
        
                        
# #     def pop_first(self):
# #         popped_node=self.head
# #         if self.length==1:
# #             self.head=None
# #             self.tail=None
# #             popped_node.next=None
# #             self.length-=1
# #         else:
# #             self.head=self.head.next
# #             self.tail.next=self.head
# #             popped_node.next=None
# #             self.length-=1
# #         return popped_node.__dict__
    
# #     # def pop(self,index=None):
# #     #     popped_node=self.tail
# #     #     if self.length==0:
# #     #         return None
# #     #     else:
# #     #         if self.length==1:
# #     #             self.head=None
# #     #             self.tail=None
# #     #         elif self.length==2:
# #     #             self.tail=self.head
# #     #             self.tail.next=self.head
# #     #         else:
# #     #             curr=self.head
# #     #             for _ in range(self.length-2):
# #     #                 curr=curr.next
# #     #             self.tail=curr
# #     #             curr.next=self.head
# #     #             popped_node.next=None
# #     #     self.length-=1
# #     def pop(self):
# #         popped_node=self.tail
# #         if self.length==0:
# #             return None
# #         elif self.length==1:
# #             self.head=None
# #             self.tail=None
# #             self.length-=1
# #         else:
# #             curr=self.head
# #             while curr.next is not self.tail:
# #                 curr=curr.next
# #             curr.next=self.head
# #             self.tail=curr
# #             popped_node.next=None
# #             self.length-=1
# #     def remove(self,idx):
# #         curr=self.head
# #         if idx>0 and idx<self.length:
# #             for _ in range(idx-1):
# #                 curr=curr.next
# #             print('Removed node:', curr.next.value)
# #             curr.next=curr.next.next
# #             if idx==self.length-1:
# #                 curr.next=self.head
# #                 self.tail=curr
# #                 self.length-=1
# #                 # self.tail.next=self.head
# #         elif idx==0:
# #             if self.length==1:
# #                 self.head=None
# #                 self.tail=None
# #             else:
# #                 self.head=curr.next
# #                 self.tail.next=self.head
# #                 curr.next=None
# #             self.length-=1
# #         else:
# #             raise IndexError("Index out of range")
                
# # csll=CSLL()
# # csll.append(10)
# # csll.append(11)
# # csll.append(12)
# # csll.prepend(13)
# # csll.prepend(111)
# # # print('CSLL: ', csll.__dict__)
# # csll.insert(0,110)
# # # print('CSLL: ', csll.__dict__)
# # csll.insert(9,'a')
# # # print(csll.pop_first())
# # # csll.pop_first()
# # # print('head: ',csll.head.__dict__)
# # # print('CSLL: ', csll.__dict__,'\n',csll)
# # print(csll)
# # # print('Head:', csll.head.__dict__)
# # # print('tail:', csll.tail.__dict__)
# # # print('length:', csll.length)
# # csll.pop()
# # print(csll)
# # print('Head:', csll.head.__dict__)
# # print('tail:', csll.tail.__dict__)
# # print('length:', csll.length)
# # csll.remove(2)
# # print(csll)
# # print('Head:', csll.head.__dict__)
# # print('tail:', csll.tail.__dict__)
# # print('length:', csll.length)


# #--------------------------------Doubly Linked List------------------------------

# # class Node:
# #     def __init__(self,value):
# #         self.prev=None
# #         self.value=value
# #         self.next=None
    
# #     # def __str__(self):
# #     #     return f'{self.prev}<- {self.value}->{self.next}'

# # class DLL:
# #     def __init__(self):
# #         self.head=None
# #         self.tail=None
# #         self.length=0
# #     def __str__(self):
# #         curr=self.head
# #         op=[]
# #         while curr:
# #             op.append(curr.value)
# #             curr=curr.next
# #         return str(op)
        
# #     def append(self,value):
# #         new_node=Node(value)
# #         if self.head is None:
# #             self.head=new_node
# #             self.tail=new_node

# #             # new_node.next=new_node
# #         # elif self.length==1:
# #         #     self.head.next=new_node
# #         #     self.tail=new_node
# #         #     self.tail.prev=self.head

# #         else:
# #             self.tail.next=new_node
# #             new_node.prev=self.tail
# #             # self.tail.prev=new_node
# #             self.tail=new_node
# #         self.length+=1
    
# #     def prepend(self,value):
# #         new_node=Node(value)
# #         if self.head is None:
# #             self.head=new_node
# #             self.tail=new_node
# #         else:
# #             self.head.prev=new_node
# #             new_node.next=self.head
# #             self.head=new_node
# #         self.length+=1
    
# #     def rev_traverse(self):
# #         curr=self.tail
# #         while curr:
# #             print(curr.value)
# #             curr=curr.prev
# # #         old po- how to purge the po/ what action needs to be taken when po is closed and item is open
# # # new po- what shld  be the communication send to  edi/business.

# #     def get(self,idx):
# #         if idx>=self.length or idx<0:
# #             return
# #         max=self.length//2
# #         if idx<max:
# #             curr=self.head
# #             for _ in range(idx):
# #                 curr=curr.next
# #             return curr
            
# #         else:
# #             curr=self.tail
# #             for _ in range(self.length-1,idx,-1):
# #                 curr=curr.prev
# #             return curr
        
# #     def set(self,idx,value):
# #         node=self.get(idx)
# #         if node:
# #             node.value=value
            
# #     def insert(self,idx,value):
# #         new_node=Node(value)
# #         if idx==0:
# #             # self.head.prev=new_node
# #             # new_node.next=self.head
# #             # new_node.prev=None
# #             # self.head=new_node
# #             self.prepend(value)
# #         elif idx==self.length:
# #             self.append(value)
# #         else:
# #             curr=self.get(idx-1)
# #             new_node.next=curr.next
# #             curr.next=new_node
# #             new_node.prev=curr
# #             new_node.next.prev=new_node
# #             # new_node.value=value
# #             self.length+=1
        
# #     def remove(self,target):
# #         curr=self.head
# #         while curr:
# #             if self.length==1:
# #                 if curr.value==target:
# #                     self.head==None
# #                     self.tail=None
# #                 else:
# #                     return
# #             else:
# #                 if curr.value==target:
# #                     curr.next.prev=None
# #                     # self.head=curr.next
# #                     curr.next=None
# #                     curr.prev=None
# #                     # curr.next.next.prev=curr.next.prev
# #                     # curr.nect.prev=None
# #             curr=curr.next
# #         self.length-=1
                    
                
        
# # dll=DLL()
# # dll.append(10)
# # dll.append(11)
# # dll.append(12)
# # dll.prepend(9)
# # dll.prepend(8)
# # dll.rev_traverse()
# # # print(dll.get(4))
# # # print('----------------------------------')
# # print(dll.set(3,122))
# # # print(dll.head,dll.head.__dict__,dll.tail,dll.tail.__dict__)
# # # print(dll.__dict__)
# # dll.insert(1,1)
# # dll.insert(dll.length,101)
# # # print(dll.head,dll.head.__dict__,dll.tail,dll.tail.__dict__)
# # # print(dll.__dict__)
# # dll.insert(0,111)
# # # curr=dll.head
# # # # print(curr.next.__dict__)
# # # for _ in range(dll.length):
# # #     print(curr.__dict__)
# # #     # print(curr.next.__dict__)

# # #     curr=curr.next
# # print(dll.head,dll.head.__dict__,dll.tail,dll.tail.__dict__, end='\n')
# # print(dll.__dict__)
# # print(dll)
# # dll.remove(9)
# # print(dll.head,dll.head.__dict__,dll.tail,dll.tail.__dict__)
# # print(dll.__dict__)
# # dll.rev_traverse()

# # print(dll)
# # # print(Node(10)

# #----------------------------- Circular Doubly Linked List -------------------------------

# class Node:
#     def __init__(self,value):
#         self.prev=None
#         self.value=value
#         self.next=None
        
# class CDLL:
#     def __init__(self):
#         self.head=None
#         self.tail=None
#         self.length=0
    
#     def __str__(self):
#         curr=self.head
#         op=[]
#         while curr:
#             op.append(curr.value)
#             curr=curr.next
#             if curr==self.head:
#                 return str(op)
            
    
#     def append(self,value):
#         new_node=Node(value)
#         curr=self.head
        
#         if curr is None:
#             self.head=new_node
#             self.tail=new_node
#             new_node.next=new_node
#             new_node.prev=new_node
        
#         else:
#             self.tail.next=new_node
#             new_node.next=self.head
#             new_node.prev=self.tail
#             self.head.prev=new_node
#             self.tail=new_node
#         self.length+=1
        
#     def insert(self,idx,value):
#         if idx<0 or idx>self.length:
#             print('index out of range')
#             return
#         new_node=Node(value)
#         curr=self.head
#         if idx==0:
#             if self.head==None:
#                 self.head=new_node
#                 self.tail=new_node
#                 self.tail.next=new_node
#                 self.head.prev=new_node
#             else:
#                 new_node.next=self.head
#                 new_node.prev=self.head.prev
#                 self.head.prev=new_node
#                 self.head=new_node
#                 self.tail.next=self.head
                
#         elif idx==self.length:
#             self.append(value)
#             return
#         else:
#             if self.head==None:
#                 self.head=new_node
#                 self.tail=new_node
#                 self.tail.next=new_node
#                 self.head.prev=new_node
#             else:
#                 for _ in range(idx-1):
#                     curr=curr.next
#                 new_node.prev=curr
#                 new_node.next=curr.next
#                 curr.next=new_node
#                 curr.next.prev=new_node
#         self.length+=1
            
# cdll=CDLL()
# # # cdll.append(10)
# # # cdll.append(12)
# # # cdll.append(13)
# # # cdll.append(14)

# cdll.insert(cdll.length,90)  
# cdll.insert(0,20)
# cdll.insert(4,111) 
        
# print(cdll.head.__dict__,cdll.tail.__dict__)
# print(cdll.__dict__)
# print(cdll)

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        current = self.head
        for _ in range(index):
            current = current.next
        return current

    def to_list(self):
        values = []
        current = self.head
        while current:
            values.append(current.value)
            current = current.next
        return values

    def copy_ll(self):
        if not self.head:
            return LinkedList()
        
        new_list = LinkedList()
        current = self.head
        while current:
            new_list.append(current.value)
            current = current.next
        return new_list

    def merge_at_index(self, index, other_ll):
        if index < 0 or index > self.length:
            raise IndexError("Index out of bounds")
        
        if not other_ll.head:
            return  # Nothing to merge if other list is empty
        
        if index == 0:
            other_ll.tail.next = self.head
            self.head = other_ll.head
        else:
            current = self.get(index - 1)
            other_ll.tail.next = current.next
            current.next = other_ll.head
        
        self.length += other_ll.length
    def remove_duplicates(self):
        curr=self.head
        nondup=[]
        dup=set()
        while curr:
            if curr.value not in nondup:
                nondup.append(curr.value)
                prev=curr
            else:
                dup.add(curr.value)
                prev.next=curr.next
            curr=curr.next
        self.tail=prev
        return self
        
def is_palindrome(lst):
    new_lst=Node(-1) #new object
    oth_lst=new_lst #new linked list
    print(oth_lst.__dict__)
    curr=lst.head #input
    # while oth_lst:
    # if curr :
    print('before:', oth_lst,curr,lst)
    print(oth_lst.__dict__)
    oth_lst.next=curr
        # curr=curr.next
        # print(oth_lst.__dict__)
        # print('after:',oth_lst.next,curr)
        # if oth_lst:
        #     print('in oth')
            # break
    return oth_lst.next

def is_palindrome(list1):
    
    curr=list1.head
    len=0
    while curr:
        curr=curr.next
        len+=1
    
    start=0
    end=len-1
    
    def get(idx,list1):
        curr=list1.head
        for _ in range(idx):
            curr=curr.next
        return curr.value
    op=[]
    while start<end:
        if get(start,ll1)==get(end,ll1):
            print('if:', get(start,ll1),get(end,ll1))
            op.append(get(start,ll1)==get(end,ll1))
            start+=1
            end-=1
            # print('if',get(start,ll1),get(end,ll1))
        else:
            print('else:', get(start,ll1),get(end,ll1))
            op.append(get(start,ll1)==get(end,ll1))
            start+=1
            end-=1
            
    return True if any(op) else False
    
def to_list(oth_lst):
    curr=oth_lst
    op=[]
    while curr:
        op.append(curr.value)
        curr=curr.next
    return op
    
def partition(ll,x):
    curr=ll.head
    ll.tail=ll.head
    while curr:
        nxtnode=curr.next
        curr.next=None
        if curr.value<x:
            ll.head=nxtnode
            nxtnode=curr
            
        
# Example Usage
ll1 = LinkedList()
ll1.append(9)
ll1.append(8)
ll1.append(12)
ll1.append(11)
ll1.append(12)
ll1.append(10)

ll2 = LinkedList()
ll2.append(1)
ll2.append(4)
ll2.append(7)
ll2.append(1)
ll2.append(4)
ll2.append(7)
ll2.append(1)
ll2.append(2)
ll2.append(4)
ll2.append(4)
# other_lst=is_palindrome(ll1)
# print(other_lst)
# print(is_palindrome(ll1),other_lst)
# print(to_list(other_lst))
# Merging ll2 into ll1 at index 2
# ll1.merge_at_index(2, ll2)
ll3=LinkedList()
ll3.generate(10,0,99)
print(ll3)
# print("Merged list:", ll1.to_list())  # Output should reflect merged lists
# print(ll1.to_list(),'\n',ll2.to_list())
print(ll2.head.__dict__,ll2.tail.__dict__)
print(ll2.remove_duplicates().to_list())
print(ll2.head.__dict__,ll2.tail.__dict__)
