# #   Created by Elshad Karimov
# #   Copyright © AppMillers. All rights reserved.

# #  Missing Number

# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]


# def missing_number(arr, n):
#     # Calculate the sum of first n natural numbers
#     total = n * (n + 1) // 2
    
#     # Calculate the sum of numbers in the array
#     sum_arr = sum(arr)
    
#     # Find the missing number by subtracting sum_arr from total
#     missing = total - sum_arr
    
#     return missing




# #  Find Pairs
# #  LeetCode 1 - Two Sum

# def find_pairs(nums, target):
#     for i in range(len(nums)):
#         for j in range(i+1, len(nums)):
#             if nums[i] == nums[j]:
#                 continue
#             elif nums[i] + nums[j] == target:
#                 print(i, j)

# myList = [1,2,3,2,3,4,5,6]
# find_pairs(myList, 6)

# # Leetcode answer
# def two_sum(nums, target):
#     seen = {}
    
#     for i, num in enumerate(nums):
#         complement = target - num
        
#         if complement in seen:
#             return [seen[complement], i]
        
#         seen[num] = i

# # Find a number
# import numpy as np 
# my_array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])

# def find_number(array, number):
#     for i in range(len(array)):
#         if array[i] == number:
#             print(i)



# # Find max product of two integer

# def max_product(arr):
#     # Initialize two variables to store the two largest numbers
#     max1, max2 = 0, 0  # O(1), constant time initialization

#     # Iterate through the array
#     for num in arr:  # O(n), where n is the length of the array
#         # If the current number is greater than max1, update max1 and max2
#         if num > max1:  # O(1), constant time comparison
#             max2 = max1  # O(1), constant time assignment
#             max1 = num  # O(1), constant time assignment
#         # If the current number is greater than max2 but not max1, update max2
#         elif num > max2:  # O(1), constant time comparison
#             max2 = num  # O(1), constant time assignment

#     # Return the product of the two largest numbers
#     return max1 * max2  # O(1), constant time multiplication

# arr = [1, 7, 3, 4, 9, 5]
# print(max_product(arr))  # Output: 63 (9*7)

# # findMaxProduct(myArray)


# # Middle
# def middle(lst):
#     # Return a new list containing all elements from the original list, excluding the first and last elements
#     return lst[1:-1]

# my_list = [1, 2, 3, 4]

# print(middle(my_list))  # Output: [2, 3]

# # 2D List
# def diagonal_sum(matrix):
#     # Initialize the sum to 0
#     total = 0

#     # Iterate through the rows of the matrix
#     for i in range(len(matrix)):
#         # Add the diagonal element to the total sum
#         total += matrix[i][i]

#     return total

# # Best Score
# def first_second(my_list):
#     max1, max2 = float('-inf'), float('-inf')

#     for num in my_list:
#         if num > max1:
#             max2 = max1
#             max1 = num
#         elif num > max2 and num != max1:
#             max2 = num

#     return max1, max2

# my_list = [84, 85, 86, 87, 85, 90, 85, 83, 23, 45, 84, 1, 2, 0]
# print(first_second(my_list))  # Output: (90, 87)

# # Duplicate Numbers
# def remove_duplicates(lst):
#     unique_lst = []
#     seen = set()
#     for item in lst:
#         if item not in seen:
#             unique_lst.append(item)
#             seen.add(item)
#     return unique_lst

# my_list = [1, 1, 2, 2, 3, 4, 5]
# print(remove_duplicates(my_list))  # Output: [1, 2, 3, 4, 5]

# # Pairs
# def pair_sum(arr, target_sum):
#     result = []
#     for i in range(len(arr)):
#         for j in range(i+1, len(arr)):
#             if arr[i] + arr[j] == target_sum:
#                 result.append(f"{arr[i]}+{arr[j]}")
#     return result

# arr = [2, 4, 3, 5, 6, -2, 4, 7, 8, 9]
# target_sum = 7
# print(pair_sum(arr, target_sum))  # Output: ['2+5', '4+3', '3+4', '-2+9']

# # Contains Duplicate
# def contains_duplicate(nums):
#     seen = set()
#     for num in nums:
#         if num in seen:
#             return True
#         seen.add(num)
#     return False

# # Example usage
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
# print(contains_duplicates(nums))  # Output: True


# #Permutation

# def permuntation(list1, list2):
#     if len(list1) != len(list2):
#         return False
#     list1.sort()
#     list2.sort()
#     if list1 == list2:  
#         return True
#     return False



# # Rotate Matrix

# def rotate(matrix):
#     n = len(matrix)

#     # Transpose the matrix
#     for i in range(n):  # Iterate over the rows
#         for j in range(i, n):  # Iterate over the columns starting from the current row 'i'
#             # Swap the elements at positions (i, j) and (j, i)
#             matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

#     # Reverse each row
#     for row in matrix:  # Iterate over each row in the matrix
#         row.reverse()  # Reverse the elements in the current row

# QQ Maximum and minimum of an array using minimum number of comparisons
# '''Input: arr[] = {3, 5, 4, 1, 9}
# Output: Minimum element is: 1
#         Maximum element is: 9

# Input: arr[] = {22, 14, 8, 17, 35, 3}
# Output: Minimum element is: 3
#         Maximum element is: 35'''
#A1
# from numpy import array
# inp=array([-11,44,-13,-111,8,-999,-44,-3])
# minim=0
# maxim=0
# for i in inp:
#     if i>=maxim:
#         maxim=i
#     elif i<=minim:
#         minim=i
# print(f"minimum num is {minim} and maximum num is {maxim}".format(minim,maxim))
# print("minimum num is {} and maximum num is {}".format(minim,maxim))

#A2
# def setmini(i):
#     curr_min=0
#     if i< curr_min:
#         curr_min=i
#     return curr_min
# def setmax(i):
#     curr_max=0
#     if i>curr_max:
#         curr_max=i
#     return curr_max
# def main():
#     from numpy import array
#     inp=array([-11,44,-13,-111,8,-999,-44,-3])
#     for i in inp:
#         print(setmax(i))
#         print(setmini(i))
# main()

# QQ Create a SLL

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
#         # print('***************In init method {self.length}************')
#         self.head = None
#         self.tail = None
#         self.length = 0
    
#     def __str__(self):
#         # print('***************In str method {self.length}************')
#         temp_node = self.head
#         result = ''
#         while temp_node is not None:
#             result += str(temp_node.value)
#             if temp_node.next is not None:
#                 result += '->'
#             temp_node = temp_node.next
#         return result
#     # def __str__(self):
#     #     current = self.head
#     #     result = []
#     #     while current is not None:
#     #         result.append(current.value)
#     #         current = current.next
#     #     return str(result)
    
#     def append(self, value):
#         new_node = Node(value)
#         if self.head is None:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             self.tail.next = new_node
#             self.tail = new_node
#         self.length += 1
#         # print(new_ll,'\n',new_ll.head.next,'\n',new_ll.tail.next)
# new_ll=LinkedList()
# new_ll.append(10)
# new_ll.append(20)
# new_ll.append(30)
# print(new_ll)

# class Node:
#     def __init__(self,value):
#         self.value=value
#         self.next=None

# class LinkedList:
#     def __init__(self):
#         self.head=None
#         self.tail=None
        
#     def __repr__(self):
#         temp_node=self.head
#         res=[]
#         while temp_node is not None:
#             res.append(temp_node.value)
#             temp_node=temp_node.next
#         return str(res)
            
#     def append(self,value):
#         new_node=Node(value)
#         if self.head is None:
#             print(f"before head {self.head}")
#             self.head=new_node
#             print(f"after head {self.head}{self.head.__dict__}")
#             print(f"before tail {self.tail}")
#             self.tail=new_node
#             print(f"after tail {self.tail}{self.tail.__dict__}")
#         else:
#             print(f"before tail.next {self.tail.next} \n{self.tail.__dict__}")
#             self.tail.next=new_node
#             print(f"after tail.next{new_node.__dict__}{self.tail.next}\n{self.tail.__dict__}")
            
#             print(f"before tail{self.tail}\n{self.tail.__dict__}")
#             self.tail=new_node
#             print(f"after tail{self.tail}\n{self.tail.__dict__}")
# new_ll=LinkedList()
# new_ll.append(10)
# new_ll.append(11)
# new_ll.append(12)
# print(new_ll,new_ll.head.next)


# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.length = 0
        
#     # Implement Here
#     def prepend(self,value):
#         new_node=Node(value)
#         if self.head==None:
#             self.head=new_node
#             self.tail=new_node
#         else:
#             new_node.next=self.head
#             self.head=new_node
#             self.length+=1
#         return self.tail.__dict__,self.head.__dict__
        
#     def append(self,value):
#         new_node=Node(value)
#         if self.head==None:
#             self.head=new_node
#             self.tail=new_node
#         else:
#             self.tail.next=new_node
#             self.tail=new_node
#         self.length+=1
        
#     def __str__(self):
#         temp_node = self.head
#         result = ''
#         while temp_node is not None:
#             result += str(temp_node.value)
#             if temp_node.next is not None:
#                 result += ' -> '
#             temp_node = temp_node.next
#         return result
        
#     # def __str__(self):
#     #     op=[]
#     #     temp=self.head
#     #     while temp is not None:
#     #         # temp=self.head
#     #         op.append(temp.value)
#     #         # if temp.next is not None:
#     #             # pass
#     #         temp=self.head.next
#     #     return str(op)
#         # temp_node=self.head
#         # res=[]
#         # while temp_node is not None:
#         #     res.append(temp_node.value)
#         #     temp_node=temp_node.next
#         # return str(res)
        
# new_ll=LinkedList()
# # new_ll.prepend(90)
# # new_ll.prepend(90)
# # new_ll.prepend(909)

# print(new_ll.prepend(909))
# print(new_ll)
# new_ll.append(99)
# new_ll.append(991)
# print(new_ll)

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail=None
        self.length = 0
        
    def __str__(self):
        temp=self.head
        op=[]
        while temp is not None:
            op.append(temp.value)
            temp=temp.next
        return str(op)
        
    def append(self,value):
        new_node=Node(value)
        if self.head==None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
        self.length+=1

    def get(self,index):
        if index>=self.length or index<0:
            return None
        else:
            temp=self.head
            for _ in range(index):
                temp=temp.next
        return temp.value
    
    def search(self,value):
        temp=self.head
        idx=0
        for _ in range(self.length):
            # print(temp.value,value,self.length,idx)
            if temp.value==value:
                return idx
            idx+=1
            temp=temp.next
        return 'Not Found'
    
    def pop(self):
        # temp=self.head
        # while temp is not None:
        popped_node=self.tail
        tail_node=self.get(self.length-2)
        self.tail= tail_node
        return popped_node.__dict__
       
    def reverse(self):
        prev_node = None
        current_node = self.head
        while current_node is not None:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        self.head, self.tail = self.tail, self.head
        
    def duplicate_check(self):
        curr=self.head
        temp=[]
        duplicates=[]
        while curr is not None:
            # print(f'checking value: {curr.value}')
            if curr.value in temp:
                # print(f'duplicate found: {curr.value}')
                duplicates.append(curr.value)
            else:
                temp.append(curr.value)
                # print(f'values seen: {temp}')
            curr=curr.next
        return duplicates if duplicates else 'No Duplicates'
    
    def remove_dup(self):
        prev=None
        curr=self.head
        non_dup=[]
        duplicates=[]
        while curr:
            # print(f'checking value: {curr.value}')
            if curr.value in non_dup:
                # print(f'duplicate found: {curr.value}')
                duplicates.append(curr.value)
                next_node=curr.next
                prev.next=next_node
                self.length-=1
            else:
                non_dup.append(curr.value)
                # print(f'values seen: {non_dup}')
                prev=curr
                self.tail=curr
            curr=curr.next
            
            # print(self.head.__dict__,self.tail.__dict__)
        return duplicates if duplicates else 'No Duplicates'
    
    def get(self,idx):
        curr=self.head
        count=0
        print(count,idx,curr)
        # while curr:
        #     if count==idx:
        #         return curr.value
        #     else:
        #         curr=curr.next
        #         count+=1
        while curr:
            if count==idx:
                print(curr,curr.__dict__)
                return curr.value
            curr=curr.next
            print(curr,curr.__dict__)
            count+=1            
    
    # def mid_node(self):
    #     print(self.length)       
    #     if self.length==0:  
    #         # print(ll,self)
    #         return None
    #     else:
    #         return self.get(self.length//2)
    def mid_node(self):
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow.__dict__
             
ll=LinkedList()
print(ll.__dict__)
ll.append('1')
ll.append('1')
ll.append('3')
ll.append('2')
ll.append('9')
ll.append('4')
ll.append('8')
print('Get method:',ll.get(2))
print('Search method:',ll.search('11'))
# print('Pop method:',ll.pop())
print(ll)    
# ll.reverse()
# print(ll)
print(ll.duplicate_check())
print(ll.remove_dup())
print(ll)
print(ll.mid_node())










