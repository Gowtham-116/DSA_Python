# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None

# class LinkedList:
#     # def __init__(self, value):
#     #     new_node = Node(value)
#     #     self.head = new_node
#     #     self.tail = new_node
#     #     self.length = 1
    
#     def __init__(self):
#         self.head = None
#         self.tail = None
#         self.length = 0
    
#     def __str__(self):
#         temp_node = self.head
#         result = ''
#         while temp_node is not None:
#             result += str(temp_node.value)
#             if temp_node.next is not None:
#                 result += ' -> '
#             temp_node = temp_node.next
#         return result
    
#     def append(self, value):
#         new_node = Node(value)
#         if self.head is None:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             self.tail.next = new_node
#             self.tail = new_node
#         self.length += 1
    
#     def prepend(self, value):
#         new_node = Node(value)
#         if self.head is None:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             new_node.next = self.head
#             self.head = new_node
#         self.length += 1
    
#     def insert(self, index, value):
#         new_node = Node(value)
#         if self.head is None:
#             self.head = new_node
#             self.tail = new_node
#         elif index == 0:
#             new_node.next = self.head
#             self.head = new_node
#         else:
#             temp_node = self.head
#             for _ in range(index-1):
#                 temp_node = temp_node.next
#             new_node.next = temp_node.next
#             temp_node.next = new_node
#         self.length += 1
    
#     def traverse(self):
#         current = self.head
#         while current is not None:
#             print(current.value)
#             current = current.next
    
#     def search(self, target):
#         current = self.head
#         while current is not None:
#             if current.value == target:
#                 return True
#             current = current.next
#         return False
    
#     def search(self, target):
#         current = self.head
#         index = 0
#         while current is not None:
#             if current.value == target:
#                 return index
#             current = current.next
#             index += 1
#         return -1
    
#     def get(self, index):
#         if index == -1:
#             return self.tail
#         elif index < -1 or index >= self.length:
#             return None
#         current = self.head
#         for _ in range(index):
#             current = current.next
#         return current
    
#     def set_value(self, index, value):
#         temp = self.get(index)
#         if temp:
#             temp.value = value
#             return True
#         return False
    
#     def pop_first(self):
#         if self.length == 0:
#             return None
#         popped_node = self.head
#         if self.length == 1:
#             self.head = None
#             self.tail = None
#         else:
#             self.head = self.head.next
#             popped_node.next = None
#         self.length -= 1
#         return popped_node
    
    
    
#     def pop(self):
#         if self.length == 0:
#             return None
#         popped_node = self.tail
#         if self.length == 1:
#             self.head = self.tail = None
#         else:
#             temp = self.head
#             while temp.next is not self.tail:
#                 temp = temp.next
#             temp.next = None
#             self.tail = temp
#         self.length -= 1
#         return popped_node
    

#     def remove(self, index):
#         if index < -1 or index >= self.length:
#             return None
#         if index == 0:
#             return self.pop_first()
#         if index == -1 or index == self.length-1:
#             return self.pop()
#         prev_node = self.get(index-1)
#         popped_node = prev_node.next
#         prev_node.next = popped_node.next
#         popped_node.next = None
#         self.length -= 1
#         return popped_node
    

#     # def remove(self, index):
#     #     prev_node = self.get(index-1)
#     #     popped_node = prev_node.next
#     #     prev_node.next = popped_node.next
#     #     popped_node.next = None
#     #     self.length -= 1
#     #     return popped_node




# linked_list = LinkedList()
# linked_list.append(10)
# linked_list.append(20)
# linked_list.append(30)
# linked_list.append(40)
# linked_list.prepend(100)
# print(linked_list)
# print(linked_list.remove(0))
# print(linked_list)


#-----------------------------CIRCULAR SINGLY LINKED LIST------------------------
class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class CSLL:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0
        
    def __str__(self) -> str:
        curr=self.head
        # print('curr',curr)
        csl=[]
        while curr:
            csl.append(curr.value)
            curr=curr.next
            # print(str(csl))
            if curr==self.head:
                return str(csl)
            #     print(str(csl))
        return str(csl)
      
    def append(self,value):
        new_node=Node(value)
        # new_node.next=new_node
        if self.head==None:
            self.head=new_node
            self.tail=new_node
            self.tail.next=self.head  #new_node.next=new_node
            self.length=1
        else:
            self.tail.next=new_node
            self.tail=new_node
            self.tail.next=self.head #new_node.next=new_node
            self.length+=1
        # print(f'{self.head}\n{self.head.next}\n{self.tail}\n{self.tail.next}-')
            
    def prepend(self,value):
        new_node=Node(value)
        if self.head==None:
            self.head=new_node
            self.tail=new_node
            self.tail.next=new_node
        else:
            # curr=self.head
            new_node.next=self.head
            self.head=new_node
            self.tail.next=new_node
        self.length+=1
        # print(f'{self.head}\n{self.head.next.__dict__}\n{self.tail.__dict__}\n{self.tail.next.__dict__}-')
        
    def insert(self,idx,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
            self.tail.next=new_node
            self.length+=1
        else:
            curr=self.head
            if idx==0:
                new_node.next=curr
                self.head=new_node
                self.tail.next=self.head
                self.length+=1
            else:
                while curr:
                    if idx>=1 and idx<self.length:
                        new_node.next=curr.next
                        curr.next=new_node
                        self.length+=1
                        break
                    if idx>self.length or idx<0:
                        try:
                            # idx=0
                            new_node.next=curr
                            self.head=new_node
                            self.tail.next=self.head
                            self.length+=1
                            # return None
                        except:
                            Exception('index out of range')
                        break
                    curr=curr.next
        # print(f'{self.head}\n{self.head.next.__dict__}\n{self.tail.__dict__}\n{self.tail.next.__dict__}*')
        
                        
    def pop_first(self):
        popped_node=self.head
        if self.length==1:
            self.head=None
            self.tail=None
            popped_node.next=None
            self.length-=1
        else:
            self.head=self.head.next
            self.tail.next=self.head
            popped_node.next=None
            self.length-=1
        return popped_node.__dict__
    
    # def pop(self,index=None):
    #     popped_node=self.tail
    #     if self.length==0:
    #         return None
    #     else:
    #         if self.length==1:
    #             self.head=None
    #             self.tail=None
    #         elif self.length==2:
    #             self.tail=self.head
    #             self.tail.next=self.head
    #         else:
    #             curr=self.head
    #             for _ in range(self.length-2):
    #                 curr=curr.next
    #             self.tail=curr
    #             curr.next=self.head
    #             popped_node.next=None
    #     self.length-=1
    def pop(self):
        popped_node=self.tail
        if self.length==0:
            return None
        elif self.length==1:
            self.head=None
            self.tail=None
            self.length-=1
        else:
            curr=self.head
            while curr.next is not self.tail:
                curr=curr.next
            curr.next=self.head
            self.tail=curr
            popped_node.next=None
            self.length-=1
    def remove(self,idx):
        curr=self.head
        if idx>0 and idx<self.length:
            for _ in range(idx-1):
                curr=curr.next
            print('Removed node:', curr.next.value)
            curr.next=curr.next.next
            if idx==self.length-1:
                curr.next=self.head
                self.tail=curr
                self.length-=1
                # self.tail.next=self.head
        elif idx==0:
            if self.length==1:
                self.head=None
                self.tail=None
            else:
                self.head=curr.next
                self.tail.next=self.head
                curr.next=None
            self.length-=1
        else:
            raise IndexError("Index out of range")
                
        
csll=CSLL()
csll.append(10)
csll.append(11)
csll.append(12)
csll.prepend(13)
csll.prepend(111)
# print('CSLL: ', csll.__dict__)
csll.insert(0,110)
# print('CSLL: ', csll.__dict__)
csll.insert(9,'a')
# print(csll.pop_first())
# csll.pop_first()
# print('head: ',csll.head.__dict__)
# print('CSLL: ', csll.__dict__,'\n',csll)
print(csll)
print('Head:', csll.head.__dict__)
print('tail:', csll.tail.__dict__)
print('length:', csll.length)
csll.pop()
print(csll)
print('Head:', csll.head.__dict__)
print('tail:', csll.tail.__dict__)
print('length:', csll.length)
csll.remove(2)
print(csll)
print('Head:', csll.head.__dict__)
print('tail:', csll.tail.__dict__)
print('length:', csll.length)