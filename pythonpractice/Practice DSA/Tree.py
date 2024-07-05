# Tree has nodes connected to each other like a parent child structure.
# Binary tree has at most 2 child

# Implement a tree

class TreeNode:
    def __init__(self,data):
        self.data=data
        self.lc=None
        self.rc=None

tt=TreeNode(10)
lc=TreeNode(11)
lcl=TreeNode(13)
lcr=TreeNode(14)
rc=TreeNode(12)
tt.lc=lc
lc.lc=lcl
lc.rc=lcr
tt.rc=rc
print(tt)

def preordertrav(rootnode):
    while rootnode is not None:
        print(rootnode.data)
        preordertrav(rootnode.lc)
        preordertrav(rootnode.rc)
        return
preordertrav(tt)
print('_'*20)

def inordertrav(rootnode):
    while rootnode is not None:
        inordertrav(rootnode.lc)
        print(rootnode.data)
        inordertrav(rootnode.rc)
        return
inordertrav(tt)
print('_'*20)

def postordertrav(rootnode):
    while rootnode is not None:
        postordertrav(rootnode.lc)
        postordertrav(rootnode.rc)
        print(rootnode.data)
        return
postordertrav(tt)

from Queue import *
# def levelordertrav(rootnode):
#     if not rootnode:
#         return
#     else:
#         que= Queue()
#         que.enqueue(rootnode)
#         while not (que.is_empty()):
#             root=que.dequeue()
#             print(root.data.data) 
#             if (root.data.lc is not None):
#                 que.enqueue(root.data.lc)
#             if (root.data.rc is not None):
#                 que.enqueue(root.data.rc)
# levelordertrav(tt)

def LevelOrderTraversal(rootnode):
    if rootnode== None:
        return
    else:
        customq=Queue()
        customq.enqueue(rootnode)
        while not(customq.is_empty()):
            root=customq.dequeue()
            # print(root.__dict__)
            print(root.data.data)
            if (root.data.lc is not None):
                customq.enqueue(root.data.lc)
            if (root.data.rc is not None):
                customq.enqueue(root.data.rc)
    
LevelOrderTraversal(tt)
    
def searchbt(rootnode,nodevalue):
    if not rootnode:
        return 'BT doesn\'t exist'
    else:
        que=Queue()
        que.enqueue(rootnode)
        # print(que.ll.head.data.data)
        while not que.is_empty():
            root= que.dequeue()
            # print(root.data.data)
            if root.data.data == nodevalue:
                return 'Success'
            if root.data.lc is not None:
                que.enqueue(root.data.lc)
            if root.data.rc is not None:
                que.enqueue(root.data.rc)
        return 'Not Found'
print(searchbt(tt,131))

def insertbt(rootnode,nodevalue):
    que=Queue()
    que.enqueue(rootnode)
    node=TreeNode(nodevalue)
    while not que.is_empty():
        root=que.dequeue()
        if root.data.lc is not None:
            que.enqueue(root.data.lc)
        else:
            root.data.lc=node
            return
        if root.data.rc is not None:
            que.enqueue(root.data.rc)
        else:
            root.data.rc=node
            return
    return nodevalue

print(insertbt(tt,15))
print('__________________________')
LevelOrderTraversal(tt)
# preordertrav(tt)
# postordertrav(tt)


def getdeepnode(rootnode):
    que=Queue()
    que.enqueue(rootnode)
    while not que.is_empty():
        root=que.dequeue()
        if root.data.lc is not None:
            que.enqueue(root.data.lc)
        if root.data.rc is not None:
            que.enqueue(root.data.rc)
            
    return root.data
print('deepest node:',end=' ')
a=getdeepnode(tt)
print(a)
        
def deletenode(rootnode, dnode):
    if not rootnode:
        return
    else:
        que=Queue()
        que.enqueue(rootnode)
        while not que.is_empty():
            root=que.dequeue()
            if root.data==dnode:
                root.data=None
                return
            if root.data.rc:
                if root.data.rc is dnode:
                    print('root.data.rc',root.data.rc)
                    root.data.rc=None
                    return
                else:
                    que.enqueue(root.data.rc)
            if root.data.lc:
                if root.data.lc is dnode:
                    print('root.data.lc',root.data.lc.data)
                    root.data.lc=None
                    return
                else:
                    que.enqueue(root.data.lc)
        
print('deleted node: ',end=' ')
print(deletenode(tt,a))
print('LevelOrderTraversal :',end= ' ')
LevelOrderTraversal(tt)
print('deleted node: ',end=' ')
print(deletenode(tt,getdeepnode(tt)))
print('LevelOrderTraversal :',end= '\n')
LevelOrderTraversal(tt)


def deletenodebt(rootnode,node):
    if not rootnode:
        return 'BT doesn\'t exist'
    
    else:
        que=Queue()
        que.enqueue(rootnode)
        while not que.is_empty():
            root=que.dequeue()
            if root.data.data==node:
                dnode=getdeepnode(rootnode)
                root.data.data=dnode.data
                deletenode(rootnode,dnode)
                return "The node is deleted"

            if (root.data.lc is not None):
                que.enqueue(root.data.lc)
            if (root.data.rc is not None):
                que.enqueue(root.data.rc)
        return "failed to delete"

print(deletenodebt(tt,10))
LevelOrderTraversal(tt)
# class Node:
#     # A utility function to create a new node
#     def __init__(self, key):
#         self.data = key
#         self.left = None
#         self.right = None

# # Function to  print level order traversal of tree
# def printLevelOrder(root):
#     # print('in print level order')
#     h = height(root)
#     for i in range(1, h+1):
#         printCurrentLevel(root, i)


# # Print nodes at a current level
# def printCurrentLevel(root, level):
#     # print('in print current level order')
#     if root is None:
#         return
#     if level == 1:
#         print(root.data, end=" ")
#     elif level > 1:
#         printCurrentLevel(root.left, level-1)
#         printCurrentLevel(root.right, level-1)


# # Compute the height of a tree--the number of nodes
# # along the longest path from the root node down to
# # the farthest leaf node
# def height(node):
#     # print('in height')
#     if node is None:
#         return 0
#     else:

#         # Compute the height of each subtree
#         lheight = height(node.left)
#         rheight = height(node.right)

#         # Use the larger one
#         if lheight > rheight:
#             return lheight+1
#         else:
#             return rheight+1


# # Driver program to test above function
# if __name__ == '__main__':
#     root = Node(1)
#     root.left = Node(2)
#     root.right = Node(3)
#     root.left.left = Node(4)
#     root.left.right = Node(5)

#     print("Level order traversal of binary tree is -")
#     printLevelOrder(root)