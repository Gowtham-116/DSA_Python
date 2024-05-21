'''from array import *
from ensurepip import version
arr=array('i',[2,3,4,5,6])
print(arr)
arr.insert(7,7)
print(5.8//1)'''
# from platform import python_version
# print(python_version())

################### 2D array #####################
# day 1 -11,23,12,13
# day 2 -21,23,22,33
# day 3 -15,20,18,17
# day 4 -19,13,22,14

from re import M
import numpy as np

twodarray=np.array([[11,23,12,13],[21,23,22,33],[15,20,18,17],[19,13,22,14],[9,39,29,19]])
#print(twodarray)
# insertion in 2d array
'''newarray=np.insert(twodarray,0,[[1,2,3,4]], axis=1)
print(newarray)
newarray1=np.insert(twodarray,0,[[1,2,3,4]], axis=0)
print(newarray1)'''

#Traversing in 2D array
'''def traverse(array):
    for i in range(len(array)): #O(mn)
        for j in range(len(array[3])): #O(n)
            print(array[i][j]) #O(1)
traverse(twodarray)'''

#searching in 2D array
'''seq=[3,2,0,None]
print([x for x in seq if x]) #prints value of x from seq only if x is true.'''

#Slicing
'''
mylist=['a','b','c','d','e','f','g']
print(mylist[1:],mylist[:3],mylist[:5:2])
mylist[:2]=['1','2']#replaces earlier elements with specified elements
print(mylist[1:],mylist[:3],mylist[:5:2])
mylist.pop(1) #.pop() removes specified index
print(mylist)
del mylist[3:5]# removes specified idex range by slicing operation
print(mylist)
mylist.remove('c')# removes specified character
print(mylist)'''

#search in a list
'''mylist=['a','b','c','d','e','f','g']
print(mylist.index(x) for x in mylist)
print(mylist.index('a')) ''' # .index() returns index number of specified element


# Sorting a list
'''lis=[1,4,7,2,6,9,3]
print(sorted(lis))
print(lis)
lis.sort()
print(lis)'''

'''i=5
while i<10:
    break
i+i
print(i)'''

#Array Project to find average temperature
'''num_of_days=int(input('How many days temperature u want?-'))
total=0
for i in range(1,num_of_days+1):
    nextday= int(input('days'+str(i)+"'s highest temperature"))
    total+=nextday
    
avg=round(total/num_of_days,2)
print(avg,'is the average temperature')'''

#Array Project to find days above average temperature
'''num_of_days=int(input('How many days temperature u want?-'))
total=0
temp=[]
for i in range(num_of_days):
    nextday= int(input('days'+str(i+1)+"'s highest temperature"))
    temp.append(nextday)
    total+=temp[i]
avg=round(total/len(temp),2)
print(avg,'is the average temperature')
count=0 
for i in temp:
    if i>avg:
        count+=1
        print(i)
print(count,'day(s) temp is more than avg temp')'''

#Missing number in an array 
# 1 Find missing number between 1 to 100
# 1+2+3+4+5+......+n = n(n+1)/2
arr=[]
for i in range(1,100):
    arr.append(i)
#for i in range(0,len(arr)):
sum=(arr[len(arr)-1]*(arr[len(arr)-1]+1))//2
print(sum,len(arr))





'''def findnum(arr):
    for i in range(len(arr)):
        if i==arr[i]:
            test.append(i)
        else:
            return i+1

arr=[]
for i in range(1,100):
    arr.append(i)
print(arr)
test=[]
print(findnum(arr))
print(test)'''













