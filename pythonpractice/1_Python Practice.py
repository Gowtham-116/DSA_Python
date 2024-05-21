# l1=[1]
# '''l1.extend((4,5))
# l1.append({6,5,6,0,2,7,8})
# print(l1)'''

# num =2
# if bool(num) == True:
#     print("true")
# else:
#     print('false')

#******************FILE I O*******************
# for i,letter in enumerate('abcde'):
#     print("At index {} the letter is {}".format(i,letter))  

# print(list(enumerate('abcde')))

# mylist1 = [1,2,3,4,5]
# mylist2 = ['a','b','c','d','e']
# print(list(zip(mylist1,mylist2)))

# st='print words starting with S string using for,if,split'
# op=[(i,j) for i in st.split(',') for j in st.split(' ') if j[0].lower()=='s']
# print(op)

#pattern programming
'''for i in range(0,5):
    for j in range(0,5):
        print(j,end=' ')
        if i==j:
            print('*',end=' ')
        if i>=j:
            print('@', end=' ')
        if i<=j:
            print('@', end=' ')
    print()'''

# create a nested list resembling 5x5 matrix
'''matrix1=[]
matrix2=[]
matrix3=[]
for i in range(0,5):
    for j in range(0,5):
        #print(j,end=' ')
        if i==j:
            print('*',end=' ')
            matrix1.append('*')
        if i>j:
            print('@', end=' ')
            matrix2.append('@')
        if i<j:
            print('@', end=' ')
            matrix3.append('@')
        
    print()
print(matrix1,matrix2,matrix3)
'''

# l1=[1,2,3,4,5]
# l2=['a','b','c','d','e']
# x=[]
# op=[[j] for i in l1 for j in l2 for k in l1 if i==k]
# # for i in range(len(x)):
# #     print(i)
# print(op)

# def myfunc(t):
#     op=''
#     for i in range(0,len(t)):
#         if i%2==0:
#             op+=t[i].upper()
#         else:
#             op+=t[i].lower()
#     return op
# print(myfunc('Anthropomorphism'))

#two sum
'''IMportant logic to compare 2 lists from different nums'''
# inp=[1,2,3,4,5,76]
# target=6
# for i in range(0,len(inp)):
#     for j in range(i+1,len(inp)-1):
#         print(i,j)
#         if inp[i]+inp[j]==target:
#             print([i,j],inp[i],inp[j])


# class Solution:
#    def twoSum(self, nums, target):
#        seen = {}
#        for i, value in enumerate(nums):
#            remaining = target - nums[i]
#            print(i,value)
           
#            if remaining in seen:
#             print(i,value) 
#             return [i, seen[remaining]]
            
#            seen[value] = i 
# print(Solution.twoSum(Solution,[1,2,3,4,5],6))

'''palindrome,factorial,fibonacci,armstrong,pattern program,
reverse a number,leap year,matrix,list,searching &sorting'''

# a=int(input())
# b=input()
# for i in range(0,a+1):
#     if b.islower():
#         d=ord(b)+a
#         if d> ord('z'):
#             op=chr(d-26)
#     else:
#         d=ord(b)+a
#         if d> ord('Z'):
#             op=chr(d-26)
# print(op)

# rinp=input()
# inp=rinp.split(" ")
#=================================AUG 1==================================
#s='HimGowthamm'

s=['hi', 'vgjhk']
# print(len(s))
# print(s[:])
# print(s[:8])
# print(s[-len(s):])
# # print(s[-10:-1:1])
# # print(s[::1])
# print(s[::-1])
# print(s[len(s):0:-1])
# print(s[::2])
# print(s[::-2])

'''print(s+' How are you!')
print(s.upper()+' How are you!'.upper(),s.lower())
print(s.upper().split('M',1))
print(s.count('m',4,13),s.find('m',1))'''

#=================================================AUG 2=====================================
'''print(s.center(21,'*'))
print('hi\tgowtham'.expandtabs())
# is check methods gives boolean output
print(s.isalnum(),s.isalpha(),s.isascii(),s.isspace(),s.islower(),s.isupper(),'Tt'.istitle())
print(s.endswith('m'))
print(s.partition('m'))'''

'''Formatting with place holders'''
# print("I'm going to inject %s here." %'something')
# print("I'm going to inject %s text here, and %s text here." %('some','more'))
# x, y = 'some', 'more'
# print("I'm going to inject %s text here, and %s text here."%(x,y))

# print('He said his name was %s.' %'Fred')
# print('He said his name was %r.' %'Fred')
# print('I once caught a fish %s.' %'this \tbig')
# print('I once caught a fish %r.' %'this \tbig')
# print('I wrote %s programs today.' %3.75)
# print('I wrote %d programs today.' %3.75) 
# print('First: %s, Second: %5.2f, Third: %r' %('hi!',3.1415,'bye!'))
# print('{0:<8} | {1:-^8} | {2:>8}'.format('Left','Center','Right'))
# print('{0:<8} | {1:-^8} | {2:>8}'.format(11,22,33))
# print('The {2} {0} {1}'.format('fox','brown','quick'))
# print('This is my ten-character, two-decimal number:%10.2f' %13.579)
# print('This is my ten-character, two-decimal number:{0:10.2f}'.format(13.579))
# num = 23.45678
# print("My 10 character, four decimal number is:{0:10.4f}".format(num))
# print(f"My 10 character, four decimal number is:{num:{10}.{6}}")

'''=========================================LISTS==================================='''
my_list = ['Gowtham',100.23,2,[3,4,5]]
# print(len(my_list),my_list[0],my_list[1:3])
# # To add item temporarily to list
# print(my_list + ['new item'],my_list)
# # Reassign to make permanent changes to list
# my_list=my_list + ['new prm item']
# print(my_list + ['new item'],my_list*2)
list1=[1,2,3,4]
# list1.append('five')
# print(list1)
# list1.extend('five')
# print(list1)
# list1.pop(len(list1)-1)
# print(list1)
#reverse() and sort() makes changes to actual list
# list1.sort()
# print(list1)
# list1.reverse()
# print(list1)

lst_1=[1,2,3]
lst_2=[4,5,6]
lst_3=[7,8,9]
matrix = [lst_1,lst_2,lst_3]
# for i in matrix:
#     print(i[0],i)
# first_col = [row[0] for row in matrix]
# print(first_col)

#list unpacking

# this lines PACKS values
# into variable a as list type
# a = ['Hi', 999, 'Prepster']

# # this lines UNPACKS values
# # of variable a
# (wel_w, num, org) = a 
# print(wel_w)
# print(num)
# print(org)
#=============================================AUG 5=====================================================
#*******************************************DICTIONARY**************************************************

# my_dict = {'key1':123,'key2':[12,23,33],'key3':['item0','item1','item2']}
# print(my_dict.values(),my_dict.keys(),my_dict.items())
# print(my_dict['key3'][0],my_dict['key3'][0].upper())    
# d = {'key1':{'nestkey':{'subnestkey':'value'}}}
# print(d['key1']['nestkey']['subnestkey'])

# d = {'k1':1,'k2':2,'k3':3}
# print(d,sorted(d.values()),d.values())
# #******************** Dict comprehension**********************
# print({x:x**2 for x in range(1,10)})
# for i,j in my_dict.items():
#     print(i,j)

# #******************Tuple**************
# t=('zero',1,2)
# print(t.index(1),t.count('zero'))

#**************Set & Boolean**********
# x=set()
# x.add(1)
# print(x)
# list1=[1,1,2,3,4,3,4,2]
# xl=set(list1)
# print(set(list1))
# # xc=x.copy()
# # print(xc,x)
# # print(xc.difference(x))
# # print(xc.difference_update(x))
# #set1.difference_update(set2)--the method returns set1 after removing elements found in set2
# #discard:Removes an element from a set if it is a member. If the element is not a member, do nothing.
# print(xl.discard(1))
# print(xl)
# print(x.union(xl),x.update(xl),x.issuperset(xl),x.issubset(xl),x.pop())

#Problem 5: Find the elements in set1 that are not in set2:
# set1 = {2,3,1,5,6,8}
# set2 = {3,1,7,5,6,8}
# print(set1.difference(set2), set1.union(set2))

# b=None
# print(b,1>2)

#**********************Files***************
# my_file = open(r'C:\Users\vgowtham2\Documents\DSA_Python\test.txt','r+')
# my_file.write('fghuihjgvbhj\n')
# my_file.seek(0)
# print(my_file.read())
# my_file.seek(0)
# print(my_file.readlines())
# print(my_file.readable())

# for line in open(r'C:\Users\vgowtham2\Documents\DSA_Python\test.txt'):
#     print(line.capitalize())

# without using try, except, finally- if any error comes then the next lines won't get executed
# p = open('oops.txt','a')
# try:
#     p.readlines()
# except:
#     print('An exception was raised!')
# finally:
#     p.close()

#with KW automatically closes the file that is opened
# with open('oops.txt','a') as p:
#     p.readlines()



#==============================================AUG 7=================================================
#***************************************loops***********************************************
#list2 = [(2,4),(6,8),(10,12)]
# list2=[[2,3],[3,4]]
# for tup in list2:
#     print(tup)
# for (t1,t2) in list2:
#     print(t1,t2)

#enumerate:enumerate is a very useful function to use with for loops. gives values in index,element format

#regular code
# index_count = 0
# for letter in 'abcde':
#     print("At index {} the letter is {}".format(index_count,letter))
#     index_count += 1

#using enumerate

# for i,letter in enumerate('abcde'):
#     print("At index {} the letter is {}".format(i,letter))

#enumerate creates index,values automatically and zip is used club two lists as a tuple if values with same index.
# print(list(enumerate('abcde')))
mylist1 = [1,2,3,4,5]
# mylist2 = ['a','b','c','d','e']
# mylist3 = ['a','b','c','d','e']
# print(list(zip(mylist1,mylist2,mylist3)))
# print(tuple(enumerate((mylist1,mylist2))))

# from random import shuffle, randint
# # This shuffles the list "in-place" meaning it won't return
# # anything, instead it will effect the list passed
# shuffle(mylist1)
# print(mylist1,randint(0,100))

#*******************************List comrehension***************************************
# Check for even numbers in a range
# lst = [x for x in range(11) if x % 2 == 0]
# print(lst)
# #nested list comp
# lst = [ x**2 for x in [x**2 for x in range(11)]]
# print(lst)


#lambda
# def myfunc(n):
#     print(n)
#     return lambda a : a * n

# mytripler = myfunc(3)

# print(mytripler(13))

























