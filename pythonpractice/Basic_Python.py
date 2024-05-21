'''a,b,c,d,e=20,10.5,20+30j,'hello hai',[1,2.3,'good',(1,2.3,'morning')]

print(e[3]*e[3])
print(e+e)
print(d+d)'''
#wap to print fibonacci number series
#0,1,1,2,3,5,8,13
f=0
s=1   
for i  in range(1,110):
    c=f+s
    s=f
    f=c
    print(i,c)

# def fib():
#     a,b=0,1
#     while True:
#         yield a
#         a,b=b,a+b
# f=fib()
# for x in f:
#     if x>55:
#         break
#     print(x)

#wap to print fibonacci number specified position
# f=0
# s=1
# num=int(input('enter pos:'))
# for i in range(0,num+1):
#     c=f+s
#     s=f
#     f=c
#     if i==num:
#         print(c)

# x = ([1,2,3], 'str',5)
# print(x)
# x[0][0]=12
# print(x)

# count=0
# add=0
# #0,1,1,2,3,5,8,13,
# for i in range(1,10):
#     add=add+i
#     count+=1
#     print(add)
#     if count==9:
#         print(add)

'''def fib(n,add,count=0):
    if count==10:
        return add
    add+=n
    count+=1
    return fib(n+1,add,count)
print(fib(1,0))'''

'''def fibonacci(n):
    a = 0
    b = 1
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(3,n+1):
            c = a + b
            a = b
            b = c
        return b
  
print(fibonacci(10))'''


'''def Fibonacci(n):
    if n<0:
        print("Incorrect input")
    elif n==1:
        return 0

    elif n==2:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)
 
print(Fibonacci(10))'''



#wap to print series of fibonacci number


# n1,n2=0,1
# i=0
# print('',n1,'\n',n2)
# #0,1,1,2,3,5,8,13,21,34,55
# for i in range(3,11):
#     fib=n1+n2
#     print(fib)
#     n1=n2

#     n2=fib
#     i+=1

# print(__file__, __name__)
'''def fib(n,add,count=0):
    if count==10:
        return add
    add+=n
    count+=1
    return fib(n+1,add,count)
print(fib(1,0))'''

'''def fibonacci(n):
    a = 0
    b = 1
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(3,n+1):
            c = a + b
            a = b
            b = c
        return b
  
print(fibonacci(10))'''




#wap to check for a palindrome in strings
'''n=input('enter a number to check palindrome or not:')
k=''
i=len(n)-1
while i<=len(n):
    k+=n[i]
    i-=1
    if i==-1:
        break
        
if k==n:
    print(n,'is a palindrome')
else:
    print(n,'is not a palindrome')'''
#using for loop
'''n=input('enter a number to check palindrome or not:')
k=''
for i in n:
    k=i+k
if k==n:
    print(n,'is a palindrome')
else:
    print(n,'are is not a palindrome')'''
#wap to check palindrome in numbers
'''m=310139
temp=m
rev=0
while temp>0:
    rem=temp%10
    temp=temp//10
    rev=rev*10+rem
if m==rev:
    print(m,'is palindrome')
else:
    print(m,'is not palindrome')'''
#Recursion

'''
rev = 0
def reverse(n):
    global rev
    if n > 0:
        rem = n % 10
        rev = rev * 10 + rem
        reverse(n//10)
    return rev

n = int(input("Enter a number:"))

num = reverse(n)
if num == n:
    print(n,"is palindrome")
else:
    print(n,"is not palindrome")'''

#armstrong or not for n digit number
'''num=int(input('enter no.'))
order=len(str(num))
sum=0
temp=num
while temp>0:
    digit=temp%10
    sum+=digit**order
    temp//=10
if num==sum:
    print(num,'is armstrong')
else:
    print(num,'is not armstrong')'''
#wap to print cubes of numbers in given range
'''n=int(input('enter last no. to find cubes:'))
for i in range(1,n+1):
        print('cube of',i,'is:',i**3)'''
#wap to print sum of squares of numbers in given list
'''a=[2,4,5,10,17]
sum=0
for i in range(0,len(a)):
    x=a[i]**2
    sum=sum+x
print('sum of squares of',a,'is:',sum)'''
#wap to convert all lc to uc
'''st='hai2hello'
x=''
for i in st:
    if 'a'<=i<='z':
        a=ord(i)-32
        x=x+chr(a)
    else:
       pass
print(x)'''

#wap to eliminate duplicates in string
'''s='haihello'
k=''
for i in s:
    if i not in k:
        k+=i
print(k)'''
#wap to print a range of prime no.
'''n=97
for i in range(2,n+1):
    flag=0
    for j in range(2,i):
        if i%j==0:
            flag=1
            break
    if flag==0:
        print(i,end=' ')
#wap to print series of prime no
l=int(input("\nenter stating no.:"))
n=int(input('enter upper range of number:'))
for i in range(l,n):
    if i==1:
        continue
    flag=0
    for j in range(2,i):
        if i%j==0:
            flag=1
    if flag==0:
        print(i,end=' ')
print()
                  #OR#
#wap to print series of prime numbers
n=2
while n<=100:
    flag=0
    for i in range(2,n):
        if n%i==0:
            flag=1
            break
    if flag==0:
        print(n,end=' ')
    n+=1
print()'''  
#wap to print nth prime number
'''n=2
m=10
count=0
while count<=m:
    flag=0
    for i in range(2,n):
        if n%i==0:
            flag=1
    if flag==0:
        count+=1
    n+=1
print(i-1)'''
'''#####'''####or######
'''n=1000000000
p=int(input('enter prime number position we want:'))
count=0
while count<=p:
    for i in range(2,n):
        flag=0
        for j in range(2,i):
            if i%j==0:
                flag=1
                break
        if flag==0:
            #print(i,end=' ')
            count+=1
            if count==p:
                 print(i)'''
#wap to print N prime numbers from any number
'''n=int(input('enter no of prime numbers to be printed:'))
m=int(input('enter starting range of prime no.'))
count=1
while count<=n:
    flag=0
    for i in range(2,m):
        if m%i==0:
            flag=1
            break
    if flag==0 and m!=1:
        print(m,end=',')
        count+=1
    m+=1'''
#wap to check given no. is perfect number(a no. whose sum of proper divisors is equal to the number) or not
'''n=28
sum=0
for i in range(1,n):
    if n%i==0:
        sum+=i
if sum==n:
    print('perfect no')
else:
    print('not a perfect no.')'''
#armstrong or not for three digit no.
'''num=370
order=len(str(num))
n=num
a=n%10
n=n//10
b=n%10
c=n//10
print(a,b,n,c)
sum=(a**3)+(b**3)+(c**3)
print(sum)
if num==sum:
    print(num,'is armstrong')
else:
    print(num,'is not armstrong')'''
#armstrong or not in given range
'''m=152
n=2000
while m<=n:
    order=len(str(m))
    dup=m
    sum=0
    while m!=0:
        temp=m%10
        m=m//10
        cube=temp**order
        sum=sum+cube
    if dup==sum:
        print(dup,'is  armstong')
    m=dup+1'''
#wap to remove duplicates in a coll
'''st='hai hello good morning'
nondup=''
for i in range(0,len(st)):
    if st[i] not in nondup:
        nondup+=st[i]
print(nondup)'''
#wap to swap k and v in a dict
'''a={1:'hai',2:(1,2)}
k=list(a)
v=list(a.values())
res={}
for i in range(0,len(a)):
    res[v[i]]=k[i]
print(res)'''
#pattern programming
'''n=5
for i in range(1,n+1):
    k=i
    for j in range(1,n+1):
        if i>=j:
            if i%2==0:
                print(k+k,end=' ')
                k+=1
            else:
                print(k,end=' ')
                k+=2
    print()'''
#equi triangle and diamond
'''n=11
for i in range (1,n+1):
    for j in range(1,n+1-i):
        print(' ',end=' ')
    for s in range(1,i+1):
        print('*',end='   ')
    print()
n=11
for i in range(1,n+1):
    for j in range(1,i+1):
        print(' ',end=' ')
    for s in range(1,n+1-i):
        print('*',end='   ')
    print()'''
#continuous side by side triangle
'''n=10
for i in range (1,n+1):
    for j in range(1,n+1-i):
        print(' ',end=' ')
    for s in range(1,i+1):
        print('*',end='   ')
    for j in range(1,(n+1-i)*2):
        print('@',end=' ')
    for s in range(1,i+1):
        print('*',end='   ')
    for x in range(1,(n+1-i)*2):
        print('@',end=' ')
    print()'''
#wap to print hollow square
'''n=10
for i in range(1,n+1):
    for j in range(1,n+2-i):
        print('*',end=' ')
    for s in range(1,i):
        print(' ',end=' ')
    for j in range(1,i):
        print(' ',end=' ')
    for s in range(1,n+2-i):
        print('*',end=' ')
    print()
for i in range(1,n+1):
    for j in range(1,i+1):
        print('*',end=' ')
    for s in range(1,n-i+1):
        print(' ',end=' ')
    for j in range(1,n+1-i):
        print(' ',end=' ')
    for s in range(1,i+1):
        print('*',end=' ')
    print()'''
#hollow rhombus 
'''n=10
for i in range(1,n+1):
    for j in range(1,n+1):
        if i+j<=n+1 or j==n or i==n:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    for j in range(1,n+1):
        if i<=j or i==n or j==1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
for i in range(1,n+1):
    for j in range(1,n+1):
        if i>=j or i==1 or j==n:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    for j in range(1,n+1):
        if i+j>=n+1 or i==1 or j==1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''
#prog to print sq of all even no. present in odd pos
'''a=[2,3,6,4,3,44,64,24,53,76,98,134]
for i in range(0,len(a)):
    if a[i]%2==0 and i%2==0:
        print(a[i]**2)'''
#wap to splt dict in form of two lists
'''a={1:2,3:4,5:6,7:8}
k=[]
v=[]
for i in a:
    k+=[i]
    v+=[a[i]]
print(k,v)'''
#wap to check str has only alpha or not
'''st='python program'
flag=0
for i in st:
    if not ('a'<=i<='z' or 'A'<=i<='Z'):
        flag=1
        break
if flag==0:
    print('only alpha')
elif flag==1:
    print('spchr or num exist')'''
#wap to all possible combinatons of a set of alphabets
'''st=''
for i in range(65,68):
    st+=chr(i)
    print(st)'''

#1)Python example for ASCII Value of a Single Character

#2)Python program to print ASCII Value of Total Characters in a String

'''st='python program'
res=''
for i in st:
    #res.append(ord(i))
    res=ord(i)
    print(res)
    
def asci(st,i=0,res=''):
    if i>=len(st):
        return res
    #res.append(ord(st[i]))
    res=res+','+str(ord(st[i]))
    return asci(st,i+1,res)
print(asci('python program'))'''


'''def reverse(st,res='',i=0):
    if i>=len(st):
        return res
    res=st[i]+res
    return reverse(st,res,i+1)
print(reverse('hai hello'))'''

#3)Python program to Concatenate Strings
'''a,b,c='hai','good','morning'
for i in a,b,c:
    print(i)'''

'''4)Python program to Convert String to Uppercase

5)Python program to Convert String to Lowercase

6)Python program to Copy a String

7)Python program to Count Occurrence of a Character in a String

8)Python program to Count Total Characters in a String'''

#9)Python program to Count Total Number of Words in a String
'''s='Python program to Count Total Characters in a String'
count=0
for i in range(0,len(s)):
    if s[i]==' ':
        count+=1
print(count+1)'''

'''s='P y t h o n p'
count=0
for i in range(0,len(s)):
    if 'a'<=s[i]<='z' or 'A'<=s[i]<='Z' or '0'<=s[i]<='9':
        continue
    else:
        count+=1
print(count)'''
#recursion
'''def char(s,count=0,i=0):
    if i==len(s):
        return count+1
    if 'a'<=s[i]<='z' or 'A'<=s[i]<='Z' or '0'<=s[i]<='9':
        pass
    else:
        count+=1
    return char(s,count,i+1)
print('no.of characters in string are:',char('p p jn on kiko'))'''

#10)Python program to Count Vowels in a String

#11)Python program to Count Vowels and Consonants in a String

'''vow,con=0,0
def vac(s,i=0):
    global vow,con
    if i==len(s):
        return vow,con
    if 'a'<=s[i]<='z' or 'A'<=s[i]<='Z':
        if s[i] in 'aeiou':
            vow+=1
        else:
            con+=1
    return vac(s,i+1)
#print((vac(s='aeiouqwr@rty')))
for j in vac(s='aeiouqwr@rty'):
    print(j)'''

#12)Python program to Count Alphabets Digits and Special Characters in a String
'''st='gowtham123@!#$9'
alpha=0
num=0
spch=0
for i in range(0,len(st)):
    if st[i].isalpha():
        print(st[i],end=' ')
        alpha+=1
    elif st[i].isnumeric():
        print(st[i])
        num+=1
    else:
        print(st[i])
        spch+=1
print(alpha,num,spch)'''
#recursion
'''def count(st='',alpha=0,num=0,spch=0,i=0):
    if i==len(st):
        print(alpha,num,spch,i)
        return alpha,num,spch,i
    if st[i].isalpha():
        alpha+=1
    elif st[i].isnumeric():
        num+=1
    else:
        spch=spch+1
    return count(st,alpha,num,spch,i+1)
print(*count('gowthallm123@!#$9k'))'''




#13)Python program to Print First Occurrence of a Character in a String
'''s='Python Program to Print First Occurrence of a Character in a String'
def focc(s,f='',i=0):
    if i==len(s):
        return f
    if s[i] not in f:
        f+=s[i]
    else:
        pass
    return focc(s,f,i+1)
print(focc(s))'''
#14)Python program to Print Last Occurrence of a Character in a String
'''s='@Pr@int suP'
def locc(s,f='',i=len(s)-1):
    if i==1:
        return f
    if s[i] not in f:
        f+=s[i]
    else:
        pass
    return locc(s,f,i-1)
print(locc(s))'''


#15)Python program to check Palindrome or Not
'''n=int(input('enter number:'))
temp=n
rev=0
while temp!=0:
    rem=temp%10
    temp=temp//10
    rev=rem+rev*10
if n==rev:
    print(n,'is palindrome')
else:
    print(n,'is palindrome')'''
#recursion
'''rev=0
def palin(n,temp,rev=0):
    global rev
    if temp!=0:
        rem=temp%10
        temp=temp//10
        rev=rem+rev*10
    return rev
n=int(input('enter number:'))
if palin(n,temp=n)==n:
    print(n,'is palindrome')'''
'''rev = 0
def palin(num):
    global rev
    if num!=0:
        rem=num%10
        rev=(rev*10)+rem
        palin(num//10)
    return rev
num=int(input("Enter your Number:"))
if(palin(num)==num):
    print(num," is a Palindrome Number.")
else:
    print(num," is not a Palindrome Number.")'''
#16)Python program to Print Characters in a String

#17)Python program to Replace Blank Space with Hyphen in a String
'''s='good morning gowtham'
sl=list(s)
st=''
for i in range(0,len(sl)):
    if sl[i]==' ':
        sl[i]='-'
        st+=sl[i]
    else:
        st+=sl[i]
print(st,type(st))
#recursion
def con(s,sl,st='',i=0):
    if i==len(sl):
        return st
    if sl[i].isspace():
        st+=sl[i].replace(' ','-')
    else:
        st+=sl[i]
    return con(s,sl,st,i+1)
''''''def conv(s,sl,st='',i=0):
    if i==len(sl):
        return st
    if sl[i]==' ':
        sl[i]='-'
        st+=sl[i]
    else:
        st+=sl[i]
    return conv(s,sl,st,i+1)''''''
s=input('st=')
print(con(s,list(s)))'''
# wap to find index of given substring in a string.
'''st=input('enter string:')
substr=input('enter substr:')
flag=False
pos=-1
count=0
n=len(st)
while True:
    pos=st.find(substr,pos+1,n) #checks b/w 0 to n in first iteration
    if pos==-1: #because we are usig find() so no further match then pos=-1 and breaks
        break
    print('found at index:',pos)
    count+=1
    flag=True
if flag==False:
    print('not found')
print('no.of occurances:',count)'''
'''for i in range(0,len(st)):
    if substr in st[i:len(st)]:
        print(st.find(substr))'''

#program to append strings alternately

'''
word1='abcxcvbnmcvcbnm'
word2='pqrjkvbn'
i=0
j=0
op=''
while i<len(word1) or j<len(word2):
    if i<len(word1):
        op=op+word1[i]
        i+=1
    if j<len(word2):
        op=op+word2[j]
        j+=1
print(op)'''

'''def mergeAlternately(word1, word2):
    string = ""
    count = 0
    while count < min(len(word1), len(word2)):
        string += word1[count]
        string += word2[count]
        count += 1
    return string + word1[count:] + word2[count:]
print(mergeAlternately('gowtham', 'varadareddy'))

from itertools import *
print(tuple(zip_longest('vhjjhbj','cghjkjhgvbghjojkhvj')))
def mergeAlternately(word1,word2):
    return"".join(x+b for x, b in zip_longest(word1, word2,fillvalue=''))
print(mergeAlternately('gowtham', 'varadareddy'))'''

'''18)Python program to Replace Characters in a String

19)Python program to Remove Odd Characters in a String'''

#20)Python program to Remove Odd Index Characters in a String

# s='gowtham'
# op=''
# op1=''
# for i in range(0,len(s)):
#     if i%2==0:
#         op=op+s[i]
#     else:
#         op1=op1+s[i]
        
# print(op,op1)

#21)Python program to Remove First Occurrence of a Character in a String


'''22)Python program to Remove Last Occurred Character in a String

23)Python program to Reverse a String

24)Python program to find String Length'''

#25)Python program to find Total Occurrence of a Character in a String
# s='aabbbcgowtham'
# counted=[]
# for i in s:
#     if i in counted:
#         continue
#     else:
#         print(s.count(i),i)
#         counted.append(i)

'''26)Python program to Toggle Characters Case in a String

1)Python example to access List Index and Values

2)Python example to add two Lists

3)Python example for Arithmetic Operations on Lists

4)Python example to check List is Empty or Not

5)Python example to Clone or Copy a List

Python program to Count Even and Odd Numbers in a List

6)Python program to Count Positive and Negative Numbers in a List

7)Python program to Print Largest Number in a List

8)Python program to Print Largest and Smallest Number'''

#9)Python program to find Length of a List
'''a=[1,2,'f','j',4,'o']
count=0
for i in a:
    count+=1
print(count,len(a))'''
'''10)Python program to find List Difference

11)Python List Multiplication Program'''

#Python program to Print Elements in a List
'''k=[1,-2,4,-6,-8,-5,7]
for i in k:
    print(i)
print('-'*44)
def ind(k,i=0):
    if i==len(k):
        return
    print(k[i])
    return ind(k,i+1)
ind(k=[1,-2,4,-6,-8,-5,7])'''
'''12)Python program to Even Numbers in a List

13)Python program to Print Odd List Numbers

14)Python program to Print Positive Numbers

15)Python program to Print Negative Numbers

16)Python program to Put Even and odd Numbers in Separate List'''

#17)Python program to Put Positive and Negative Numbers in Separate List
'''k=[1,-2,4,-6,-8,-5,7]
neg=[]
pos=[]
for i in k:
    if i<0:
        neg+=[i]
    elif i>0:
        pos+=[i]
print(neg,',',pos)'''
#recursion
'''def sep(k,neg=[],pos=[],i=0):
    if i==len(k):
        return neg,pos
    if k[i]<0:
        neg+=[k[i]]
    elif k[i]>0:
        pos+=[k[i]]
    return sep(k,neg,pos,i+1)
for j in sep(k=[1,-2,4,-6,-8,-5,7]):
    print(j)'''

'''18)Python program to Remove Duplicates from List

19)Python program to Remove Even Numbers in a List

20)Python program to Reverse List Items'''

#21)Python program to Print Second Largest Number in a List

# print('xgfhj')
# a=[2,1,5,3,6,8]
# for i in range(1,len(a)):
#     for j in range(0,len(a)-i):
#         if a[j]>a[j+1]:
#             a[j],a[j+1]=a[j+1],a[j]
# print(a)
# inp=int(input('enter the max position of number :'))
# n=len(a)-inp
# print('{} largest number is {}'.format(abs(inp),a[n]))


# a=[1,2,3,4,5,6]
# for i in range(0,len(a)):
#     for j in range(0,len(a)-i):
#         if a[j]>a[j+1]:
#             a[j],a[j+1]=a[j+1],a[j]
#22)Python program to Sort Elements in Ascending Order.

#23)Python program to Print Smallest Element in a List.

'''24)Python program to find Sum of All Elements

25)Python program to find Sum of Even and Odd Numbers in a List'''

#wap to perform basic arithmatic operations
'''def add(a,b):
    print(a+b)
def sub(a,b):
    print(a-b)
def prod(a,b):
    print(a*b)
def floor(a,b):
    print(a/b)
def mod(a,b):
    print(a%b)
    print(a//b)
a=float(input())
b=int(input())
add(a,b)
sub(a,b)
prod(a,b)
floor(a,b)
mod(a,b)'''

#sum of digits
# val=111
# op=0
# while True:
#     rem=val%10
#     op=op+rem
#     val=val//10
#     if 0==val:
#         break
# print(op)  

#Happy number

# def ishappy(n):
#     past=set()
#     while n!=1:
#         n=sum(int(i)**2 for i in str(n))
#         if n in past:
#             return False
#         past.add(n)
#     return False
# print(ishappy(6))

#valid brackets
# Python3 code to Check for
# balanced parentheses in an expression
'''def check(expression):
	open_tup = tuple('({[')
	close_tup = tuple(')}]')
	map1 = dict(zip(open_tup, close_tup))
	queue = []
    
	for i in expression:
		if i in open_tup:
			queue.append(map1[i])
			print(queue,'-Q')
		elif i in close_tup:
			if not queue or i != queue.pop():
				return "Unbalanced"
	if not queue:
		return "Balanced"
	else:
		return "Unbalanced"

# Driver code
string = "{[]{()}}"
print(string, "-", check(string))

string = "((()"
print(string,"-",check(string))'''

    
    


########################FUNCTIONS#########################################################################
#wap to extract all sp char in a given str b/w si and ei
'''def spch(st,si=0,ei=None):
    if ei==None:
        ei=len(st)
    print(ei,si)
    spch=''
    for i in range (0,len(st)):
        if si<=i<=ei and not ('a'<=st[i]<='z' or 'A'<=st[i]<='Z' or '0'<=st[i]<='9'):
            #print(st[i],end=' ')
            spch+=st[i]
    return spch
print(spch('g()()d m()rn!ng g@wth@^^',5,24))'''
#wap to convert all LC to UC char b/w si and ei
'''def up(st,si=0,ei=None):
    if ei==None:
        ei=len(st)
    res=''
    for i in range(0,len(st)):
        if si<=i<=ei and 'a'<=st[i]<='z':
            res+=chr(ord(st[i])-32)
        else:
            res+=st[i]
    return res
print(up('hello HI gowtham',3))'''
#wap to print fact of a number using recursion
'''def fact(n):
    if n in (1,0):
        return 1
    return n*fact(n-1)
n=int(input('enter'))
print(n,'factorial is:',fact(n))'''
#wap to reverse the string
#using for loop
'''st='gowtham'
rev=''
for i in st:
    rev=i+rev
print(rev)
#using while loop
st='gowtham'
i=0
re=''
while i<len(st):
    re=st[i]+re
    i+=1
print(re)'''
#using recursion
'''def reverse(st,i=0,reve=''):
    if i>=len(st):
        return reve
    reve=st[i]+reve
    return reverse(st,i+1,reve)
print(reverse('gowtham',i=3))'''
#wap to print series of prime no.
'''n=100
for i in range(2,100):
    flag=0
    for j in range(2,i):
        if i%j==0:
            flag=1
            break
    if flag==0:
        print(i,end=' ')'''
#using recursion
'''i=1
def prime(i,n=100):
    print(i)
    if i==n:
        return
    print(i)
    flag=0
    for j in range(2,i):
        print(i,j)
        if i%j==0:
            flag=1
    if flag==0:
        print(i,end=' ')
prime(i+1)'''
#using recursion
'''def CheckPrime(i,num):
    if num==i:
        return 0
    else:
        if(num%i==0):
            return 1
        else:
            return CheckPrime(i+1,num)
n=100
print("Prime Number Between 1 to n are: ")
for i in range(2,n+1):
    if(CheckPrime(2,i)==0):
        print(i,end=',')'''
#
'''T = int(input())
L = []
for t in range(T):
    args =input().split(" ")
    if args[0] == "append":
        L.append(int(args[1]))
    elif args[0] == "insert":
        L.insert(int(args[1]), int(args[2]))
    elif args[0] == "remove":
        L.remove(int(args[1]))
    elif args[0] == "pop":
        L.pop()
    elif args[0] == "sort":
        L.sort()
    elif args[0] == "reverse":
        L.reverse()
    elif args[0] == "print":
        print (L) '''

'''T = int(input())
L = []
for t in range(T):
    args =input().split(" ")
    if args[0] == "append":
        L.append(int(args[1]))
    elif args[0] == "insert":
        L.insert(int(args[1]), int(args[2]))
    elif args[0] == "remove":
        L.remove(int(args[1]))
    elif args[0] == "pop":
        L.pop()
    elif args[0] == "sort":
        L.sort()
    elif args[0] == "reverse":
        L.reverse()
print(L) '''
#wap to print * triangle
'''n=5
for i in range(1,n+1):
    for j in range(1,n+1):
        if i>=j:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''
#recursion
'''def inn(n,i,j=1):
    if j==n+1:
        return
    if i>=j:
        print('*',end=' ')
    else:
        print(' ',end=' ')
    inn(n,i,j+1)
def out(n,i=1):
    if i==n+1:
        return
    inn(n,i)
    print()
    out(n,i+1)
out(5)'''

#max candies

# def kidsWithCandies(candies, extraCandies):
#     maxNumCandies = max(candies)
#     print(dict(enumerate(candies)))
#     for idx, candy in enumerate(candies):
#         canHaveMaxCandies = (candy + extraCandies) >= maxNumCandies
#         candies[idx] = canHaveMaxCandies
#         print(candies)
#     return candies
# print(kidsWithCandies([2,4,1,4,3],2))

#reverse words of str
# def reverseWords(s):
#     lis=s.split(' ')
#     op=[]
#     for i in range(0,len(lis)):
#         print(lis[i],i)
#         op.append(lis[i])
#     return ' '.join(reversed(op))
# print(reverseWords('sky is blue'))

# l='sky is    blue'
# li=l.split()
# print(li)
#wap to print details of car
'''class car:
    company_name='Ferrari'
    headquaters='italy'
    ceo='john elkann'
    founded=1947
    def __init__(self,mname,fuel_economy,colour):
        self.mname=mname
        self.fuel_economy=fuel_economy
        self.colour=colour
m1=car('ferrari812',7,'white')
m2=car('ferrarif8',8,'red')
print('details of m1:',car.company_name,car.headquaters,m1.mname,m1.colour)
print('details of m2:',car.company_name,car.headquaters,m2.mname,m2.colour)'''
#wap to print details of student.
'''class stu:
    degree='b.tech'
    spec='civil engg'
    sec=1
    def __init__(self,name,sid,email,phno,fee,grade):
        self.name=name
        self.sid=sid
        self.phno=phno
        self.email=email
        self.fee=fee
        if type(grade)==str:
            self.grade=grade
    def ch_name(self,ch_name):
        self.name=ch_name
    def ch_sid(self,stuid):
        self.sid=stuid
    def ch_grade(self,sgrade):
        if type(sgrade)==str:
            self.grade=sgrade
    def ch_email(self,s_email):
        self.email=s_email
    def ch_phno(self,s_phno):
        self.phno=s_phno
        self.msg()
    def disp(self):
        print(' degree:',stu.degree,'\n','spec:',stu.spec,'\n','sec:',stu.sec,'\n','name:',self.name)
        print(' id:',self.sid,'\n','phno:',self.phno,'\n','email:',self.email,'\n','fee:',self.fee,'\n','grade:',self.grade)
    @classmethod
    def display(cls):
        print('',stu.degree,'\n',stu.spec,'\n',stu.sec)
    @classmethod
    def ch_degree(cls,newdeg):
        cls.msg()
        cls.degree=newdeg
        
    @classmethod
    def ch_spec(cls,newspec):
        cls.spec=newspec
    @classmethod
    def ch_sec(cls,newsec):
        cls.sec=newsec
    @staticmethod
    def msg():
        print(' done')
b=stu('B','16f6','sdf@gmail.com',22222222,10000,'s')
b.disp()
stu.ch_grade(b,'d')
stu.ch_phno(b,99999999999999)
print('----------------------------')
stu.disp(b)
stu.msg()
print('----------------------------')
stu.ch_degree('dddddddddddddddddd')
stu.display()'''

#create a class to store details of indian cricketers.

'''class cric:
    org='bcci'
    president='s ganguly'
    captain='v kohli'
    __revenue='2.4billion'
    def __init__(self,name,jno,place,sal,dyr):
        self.name=name
        self.jno=jno
        self.place=place
        self.dyr=dyr
        self.__sal=sal
    def disp(self):
        print(cric.org,cric.president,cric.captain,cric.__revenue)
        print('-'*44)
        print(self.name,self.jno,self.place,self.dyr,self.__sal)
vk=cric('vk',13,'punjab',3000000,2008)
vk.disp()'''

'''class emp:
    cname='pysp'
    mbl='bglr'
    ceo='ak'
    def __init__(self,name,phno,sal):
        self.name=name
        self.phno=phno
        self.__sal=sal
    def __disp(self):
        print(self.name,self.phno,self.__sal)
vk=emp('vk',3000000,2008)
vk.__disp()'''


'''class A:
    __a=10
    _b=20
    def __init__(self,c,d):
        self.c=c
        self.__d=d
        print(self.__d)
    def __disp(self):
        print(id(self))
        print(self.c,self.__d)
    @classmethod
    def _display(cls):
        print(cls.__a,cls._b)
    @staticmethod
    def __success():
        print('successful')
    @classmethod
    def get(cls):
        print(id(cls),'-------------------')
        return cls.__a
    @classmethod
    def getter(cls):
        print(id(cls),'-----------')
        return cls.__disp
oa=A(30,40)

res=A.get()
print(res)
out=A.getter()
out(oa)
print(id(A),'-----------------')
print(oa.c)'''

#Abstraction
'''from abc import ABC,abstractmethod
class Ademo(ABC):
    @abstractmethod
    def disp(self):
        pass
    @classmethod
    @abstractmethod
    def display(cls):
        pass
class cc(Ademo):
    def disp(self):
        print('concrete class')
    @classmethod
    def display(cls):
        print('classmethod')
oa=cc()
oa.disp()
oa.display()'''

'''
import re
a='V Gowthamv   gowtham2020-10-232021/11/25gowthamreddy_99v@gmail.comgowtham-red@outlook.in\ngowtham.in@yahoomail.org'
b='hello'
match=re.findall('\s',a)

for i in match:
    #print('the match \"{x}\" in the span is{y} in the string \"{z}\"'.format(y=i.span(),x=i.group(),z=a))
    print(i,len(i))'''


#############################------DATA STRUCTURES--------###################

#MERGE SORT

'''def mergesort(list1):
    if len(list1)>1:
        mid=len(list1)//2
        leftlist=list1[:mid]
        rightlist=list1[mid:]
        mergesort(leftlist)
        mergesort(rightlist)
        i=0
        j=0
        k=0
        while len(rightlist)>j and len(leftlist)>i:
            if leftlist[i]<rightlist[j]:
                list1[k]=leftlist[i]
                i+=1
                k+=1
            else:
                list1[k]=rightlist[j]
                j+=1
                k+=1
            
        while len(leftlist)>i:
            list1[k]=leftlist[i]
            i+=1
            k+=1
                
        while len(rightlist)>j:
            list1[k]=rightlist[j]
            j+=1
            k+=1

num=int(input('length of list:'))
list1=[int(input()) for x in range(num)]
mergesort(list1)
print('sorted list:',list1)'''





##########################OOPS#########################

'''
class student:
    cname='sietk'
    loc='puttur'
    cm='ar'
    def __init__(self,sname,roll,dept,hod,sec):
        self.sname=sname
        self.roll=roll
        self.dept=dept
        self.hod=hod
        self.sec=sec
    def disp(self):
        print('cname:',self.cname,'\nloc:',self.loc,'\ncm:',self.cm,'\nsname',self.sname,'\nroll:',self.roll,'\ndept:',self.dept,'\nhod:',self.hod,'\nsec:',self.sec)
    def ch_hod(self,new_hod):#OBJECT METHOD
        self.hod=new_hod
    @classmethod
    def ch_cm(cls,new_cm):#CLASS METHOD
        cls.cm=new_cm


class faculty(student):
    print('cname:',student.cname)

class faculty:
    print('2 program')
    #print(student.cname)
    #super().__init__(self)
    #print(self.sname)
faculty()



gowtham=student('gowtham',116,'ce','siva',1)#OBJECT CREATION
k=student('k',111,'ee','raj',2)#OBJECT CREATION
#a=student()#cant use this when using init method
#student.method(args)


#student.disp(gowtham)
print('GOWTHAM details:')
gowtham.disp()
#k.disp()
print('-'*50)
k.ch_hod('pyh')
student.ch_cm('rj')
 
k.disp()
print('-'*50)
gowtham.disp()


'''


















