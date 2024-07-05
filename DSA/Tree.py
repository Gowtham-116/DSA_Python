#-------------------------- Tree using python list---------------------

# class Treenode:
#     def __init__(self,data,children=[]):
#         self.data=data
#         self.children=children
    
#     def __str__(self,level=0):
#         ret = "  " * level + str(self.data)  + "\n"
#         for child in self.children:
#             ret += child.__str__(level + 1)
#         return ret
    
#     def addchild(self,Treenode):
#         self.children.append(Treenode)

# tree=Treenode('Drinks',[])
# cold=Treenode('cold',[])
# hot=Treenode('hot',[])
# tree.addchild(cold)
# tree.addchild(hot)        
# tea = Treenode('Tea', [])
# coffee = Treenode('Coffee', [])
# cola = Treenode('Cola', [])
# fanta = Treenode('Fanta', [])
# cold.addchild(cola)
# cold.addchild(fanta)
# hot.addchild(tea)
# hot.addchild(coffee)
# print(tree.__dict__)


#-------------------Binary tree: Two child for each node---------------------
import QueueLinkedList as queue
class TreeNode:
    def __init__(self,data):
        self.data=data
        self.lc=None
        self.rc=None
        
    # def __str__(self,level=0):
    #     root=self.data
    #     while root:
    #         print(root)
    #         root=self.lc
    #         print(root)
    #         root=self.rc
    #         print(root)
            
        
bt=TreeNode('Drinks')
lc=TreeNode('cola0')
lcl=TreeNode('cola1')
lcr=TreeNode('cola2')
lcll=TreeNode('cola3')
lclr=TreeNode('cola4')
rc=TreeNode('coke')
bt.lc=lc
bt.rc=rc
lc.lc=lcl
lcl.lc=lcll
lcl.rc=lclr
lc.rc=lcr

# def PreorderTrav(rootnode):
#     if not rootnode:
#         return
#     print(rootnode.data)
#     PreorderTrav(rootnode.lc)
#     PreorderTrav(rootnode.rc)
# PreorderTrav(bt)
# print(bt.lc.__dict__)

# def InOrderTrav(rootnode):
#     if rootnode==None:
#         return 
#     InOrderTrav(rootnode.lc)
#     print(rootnode.data)
#     InOrderTrav(rootnode.rc)
# InOrderTrav(bt)

# def PostOrderTrav(rootnode):
#     if rootnode==None:
#         return 
#     PostOrderTrav(rootnode.lc)
#     PostOrderTrav(rootnode.rc)
#     print(rootnode.data)
# PostOrderTrav(bt)

def LevelOrderTraversal(rootnode):
    if rootnode== None:
        return
    else:
        customq=queue.Queue()
        customq.enqueue(rootnode)
        while not(customq.isEmpty()):
            root=customq.dequeue()
            print(root.value.data)
            if (root.value.lc is not None):
                customq.enqueue(root.value.lc)
            if (root.value.rc is not None):
                customq.enqueue(root.value.rc)
    
LevelOrderTraversal(bt)


def searchBT(rootnode,nodevalue):
    if not rootnode:
        return "BT doesn't exist"
    else:
        customqueue=queue.Queue()
        customqueue.enqueue(rootnode)
        # print(customqueue.linkedList.head.value.lc.data)
        while not(customqueue.isEmpty()):
            root=customqueue.dequeue()
            if root.value.data==nodevalue:
                return "success"
            if (root.value.lc is not None):
                customqueue.enqueue(root.value.lc)
            if (root.value.rc is not None):
                customqueue.enqueue(root.value.rc)
        return "not found"
print('--------------------')
print(searchBT(bt, 'cola3'))

def insertBT(rootnode,newnode):
    if str(newnode)==newnode:
        newnode=TreeNode(newnode)
    if not rootnode:
        rootnode=newnode
    else:
        customqueue=queue.Queue()
        customqueue.enqueue(rootnode)
        while not (customqueue.isEmpty()):
            root=customqueue.dequeue()
            if root.value.lc is not None:
                customqueue.enqueue(root.value.lc)
            else:
                root.value.lc=newnode
                return "Inserted at lc"
            if root.value.rc is not None:
                customqueue.enqueue(root.value.rc)
            else:
                root.value.rc=newnode
                return "Inserted at rc"

newnode=TreeNode('coke1')
print(insertBT(bt,newnode))
print(insertBT(bt,TreeNode('coke2')))
print(insertBT(bt,'newnode'))
# print(bt)
LevelOrderTraversal(bt)

def getdeepestnode(rootnode):
    que=queue()
    
    
    
    
# def height(rootnode):
#     if not rootnode:
#         return 0
#     lht=rht=0
    
#     if rootnode is not None:
#         rootnode=rootnode.lc
#         height(rootnode)
#         lht+=1

#     if rootnode is not None:
#         rht+=1
#         rootnode=rootnode.lc
#         height(rootnode)
#     return lht if lht>rht else rht
# print(height(bt))



# def height(node):
#     if node is None:
#         return 0
#     else:
#         # Compute the height of each subtree
#         lheight = height(node.lc)
#         rheight = height(node.rc)
#         # Use the larger one
#         if lheight > rheight:
#             print(lheight)
#             return lheight+1
#         else:
#             print(rheight)
#             return rheight+1
        
# print(height(bt))