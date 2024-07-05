# # # Stack with python list
# # class stack:
# #     def __init__(self):
# #         self.list=[]
    
# #     def __str__(self):
# #         rev_list=reversed(self.list)
# #         values=[str(x) for x in rev_list]
# #         return '\n'.join(values)
        
# #     def append(self,value):
# #         self.list.append(value)
    
# #     def isEmpty(self):
# #         if self.list==[]:
# #             return True
# #         else:
# #             return False
# #     def pop(self):
# #         if self.isEmpty():
# #             return 'Empty list'
# #         else:
# #             return (self.list.pop())
    
# #     def peek(self):
# #         if self.isEmpty():
# #             return 'None'
# #         else:
# #             return self.list[len(self.list)-1]   
    
# # s=stack()
# # print(s.pop())
# # print(s.isEmpty())
# # s.append(10)
# # s.append(20)
# # s.append(30)
# # print(s.isEmpty())
# # print(s.pop())
# # print(s.peek())
# # print(s)

# # Stack with list with size limit

# class stacklimit:
    
#     def __init__(self,size):
#         self.size=size
#         self.list=[]
        
#     def __str__(self):
#         # print(self.__dict__)
#         values=[str(x) for x in self.list]
#         return '\n'.join(values)        
    
#     def isEmpty(self):
#         if self.list==[]:
#             return True
#         else:
#             return False
        
#     def push(self,value):
#         if len(self.list)==self.size:
#             return 'Stack is full'
#         else:
#             self.list.append(value)
#             return 'Inserted successfully'
        
#     def pop(self):
#         if self.list==[]:
#             return 'Empty list'
#         else:
#             return self.list.pop()
            
# s=stacklimit(4)
# s.push(10)
# s.push(11)
# s.push(12)
# s.pop()
# s.push(13)
# s.push(14)
# print(s)

# Stack using linked list

# class Node:
#     def __init__(self,value):
#         self.value=value
#         self.next=None

# class LinkedList:
#     def __init__(self):
#         self.head=None
    
# class StackLL:
#     def __init__(self):
#         self.linkedlist=LinkedList()
        
#     def __str__(self):
#         curr=self.linkedlist.head
#         op=[]
#         while curr:
#             if curr is not None:
#                 op.append(curr.value)
#             curr=curr.next
#         values=[str(x) for x in op]
#         return '\n'.join(values)
    
#     # def __iter__(self):
#     #     curNode = self.head
#     #     while curNode:
#     #         yield curNode.__dict__
#     #         curNode = curNode.next
            
    
#     def push(self,value):
#         new_node=Node(value)
#         new_node.next=self.linkedlist.head
#         self.linkedlist.head=new_node
        
#     def pop(self):
#         popped_node=self.linkedlist.head
#         self.linkedlist.head=popped_node.next
#         popped_node.next=None
#         return popped_node.__dict__
    
#     def delete(self):
#         self.linkedlist.head=None
#         return 'list is empty'

# s=StackLL()
# s.push(10)
# s.push(11)
# s.push(12)
# # s.pop()
# s.push(13)
# s.push(14)
# print(s)
# print(s.pop())
# print(s)
# print(s.delete())
# print(s)


#create stack using LL
class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
    
class StackLL:
    def __init__(self):
        # self.linkedlist=LinkedList()
        self.head=None
        
    def __str__(self):
        curr=self.head
        op=[]
        while curr:
            if curr is not None:
                op.append(curr.value)
            curr=curr.next
        values=[str(x) for x in op]
        return '\n'.join(values)
    
    # def __iter__(self):
    #     curNode = self.head
    #     while curNode:
    #         yield curNode.__dict__
    #         curNode = curNode.next
            
    def push(self,value):
        new_node=Node(value)
        new_node.next=self.head
        self.head=new_node
        
    def pop(self):
        popped_node=self.head
        self.head=popped_node.next
        popped_node.next=None
        return popped_node.__dict__
    
    def delete(self):
        self.head=None
        return 'list is empty'

s=StackLL()
s.push(10)
s.push(11)
s.push(12)
# s.pop()
s.push(13)
s.push(14)
print(s)
print(s.pop())
print(s)
# print(s.delete())
print(s.head.next.__dict__)


