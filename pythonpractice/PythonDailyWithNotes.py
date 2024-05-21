#********DAY 1-11/28/2022********
# Python coding question:
# Given a list of integers, return True if the array contains a 3 next to a 3 somewhere.
# Desired output:
# has_33([1, 3, 3]) → True
# has_33([1, 3, 1, 3]) → False
# has_33([3, 1, 3]) → False
# has_33([3,3,1]) → True

# def has_33(list1):
#     for i in range(len(list1)):
#         if list1[i:i+2]==['3','3']:
#             print(list1[i])
#             return 'true'
#         else:
#             pass
# inp=input('enter numbers seperated by comma:')
# list1=[]
# list1.append(inp.split(sep=','))
# print(has_33(list1[0]))

#=================================Day 2 11/29/2022 ============================
#Q1
# Input data contain number of test-cases in the first line.
# Then the specified number of lines follows each representing one test-case.
# Lines consist only of lowercase English (Latin) letters and spaces.
# Answer should contain the number of vowels in each line, separated by spaces.

# inp=int(input('enter num of strings:'))
# listofstrings=[]
# for i in range(inp):
#     strin=input()
#     listofstrings.append(strin)
# count=0
# for i in range(len(listofstrings)):
#     count=0
#     for j in range(len(listofstrings[i])):
#         if listofstrings[i][j].lower() in ['a','e','i','o','u']:
#             count+=1
#     print(count, sep=' ')

#=================================Day 3 11/30/2022 ============================
#Q1 check leap year or not

# def is_leap(year):
#     leap = False
#     if (year%4) == 0:
#         if (year%100) == 0:
#             if (year%400) == 0:
#                 leap = True
#         else:
#             leap = True        
#     return leap
# year = int(input())
# print(is_leap(year))

#=================================Day 3 12/01/2022 ============================
#Q1 Two sum==> return index of two numbers whose sum equals to target

# class Solution:
#     def twosum(self, nums, target):
#         seen={}
#         for i,value in enumerate(nums):
#             remaining=target-nums[i]
#             if remaining in seen:
#                 return[i,seen[remaining]]
#             seen[value]=i

# nums=[int(item) for item in input().strip().split(' ')]
# print(nums)
# a=enumerate(nums)
# # enumerate(iterable, start=any num used as index) gives a list of tuples with index
# # followed by value from iterable , enum() needs to be type casted to list to display or
# # we can use loops to display index and value like in this example
# print(list(a))
# target=int(input())
# print(Solution.twosum(Solution,nums,target))

# def halvesAreAlike(s: str) -> bool:
#         vowel=['a','e','i','o','u','A','E','I','O','U']
#         a=''
#         b=''
#         ca=0
#         cb=0
#         a=s[:len(s)//2]
#         b=s[len(s)//2:]
#         print(a,b)
#         for j in range(0,len(a)):
#             if a[j] in vowel:
#                 ca+=1
#                 print(a[j],ca)
#             if b[j] in vowel:
#                 cb+=1
#                 print(b[j],cb)
#         return ca==cb

# print(halvesAreAlike('textbook'))

#=================================Day 4 12/02/2022 ============================
# if __name__ == '__main__':
#     x = int(input())
#     y = int(input())
#     z = int(input())
#     n = int(input())
# cord=[[i,j,k] for i in range(0,x+1) for j in range(0,y+1) for k in range(0,z+1)]
# op=[]
# for i in range(0,len(cord)):
#     if sum(cord[i])!=n:
#         op.append(cord[i])
# print(op)


#=================================Day 5 12/05/2022 ============================
'''
class Person:
    def __init__(self,initialAge):
        self.initialAge=initialAge
        # Add some more code to run some checks on initialAge\
        if self.initialAge<0:
            self.initialAge=0  
        else:
            self.initialAge=initialAge
    def amIOld(self):
        # Do some computations in here and print out the correct statement to the console
        if self.initialAge<13:
            print('You are young..')
        elif self.initialAge>=13 and self.initialAge<18:
            return 'You are a teenager..'
        else:
            return 'You are old..'
    def yearPasses(self):
        # Increment the age of the person in here
        self.initialAge=self.initialAge+1
        return self.initialAge
t = int(input())
for i in range(0, t):
    age = int(input())         
    p = Person(age)  
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()       
    p.amIOld()
    print("")
'''

#Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.
#print([x for x in range(1,51) if x%3==0])

'''Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead
 of the number, and for the multiples of five print "Buzz". For numbers which are multiples of both three 
 and five print "FizzBuzz".'''

# for i in range(1,101):
#     if i%3==0 & i%5==0:
#         print('fizzbuzz')
#     elif i%3==0:
#         print('fizz')
#     elif i%5==0:
#         print('buzz')
#     else:
#         print(i)

'''Guessing Game Challenge
Let's use while loops to create a guessing game.

The Challenge:

Write a program that picks a random integer from 1 to 100, and has players guess the number. The rules are:

If a player's guess is less than 1 or greater than 100, say "OUT OF BOUNDS"
On a player's first turn, if their guess is
within 10 of the number, return "WARM!"
further than 10 away from the number, return "COLD!"
On all subsequent turns, if a guess is
closer to the number than the previous guess return "WARMER!"
farther from the number than the previous guess, return "COLDER!"
When the player's guess equals the number, tell them they've guessed correctly and how many guesses it took!
'''

# below sol fails to check if new guess is closer than old guess or not
'''from random import randint
i=randint(1,100)
print(i)
inp=int(input('enter a number of ur choice:'))
guess=0
while i!=inp:
    
    if inp>100 or inp<1:
        print('ERROR!!: OUT OF BOUNDS')
        break
    elif inp in range(i-10,i+11):
        print('WARM!')
    elif inp<i-10 or inp>i+10:
        print('COLD!')
    guess+=1
else:
    print('Num guess is correct, took {} tries'.format(guess+1))'''

#####SOL 2
'''
import random
num = random.randint(1,100)
print(num)
guesses=[0]
while True:
    guess = int(input("I'm thinking of a number between 1 and 100.\n  What is your guess? "))
    if guess < 1 or guess > 100:
        print('OUT OF BOUNDS! Please try again: ')
        continue
    # here we compare the player's guess to our number
    if guess == num:
        print(f'CONGRATULATIONS, YOU GUESSED IT IN ONLY {len(guesses)} GUESSES!!')
        break
    # if guess is incorrect, add guess to the list
    guesses.append(guess)
    # when testing the first guess, guesses[-2]==0, which evaluates to False
    # and brings us down to the second section
    print(guesses)
    if guesses[-2]:  
        if abs(num-guess) < abs(num-guesses[-2]):
            print('WARMER!')
        else:
            print('COLDER!')
    else:
        if abs(num-guess) <= 10:
            print('WARM!')
        else:
            print('COLD!')
'''


#***********************has Alternating bits*************************
'''n=11
binary=bin(n)[2:]
print(binary)
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        binary=bin(n)[2:]
        for i in range(len(binary)-1):
            if (binary[i]==binary[i+1]):
                return False
        return True'''



#check if guessed number is closer or not
# import random
# num = random.randint(1,100)
# print(num)
# guesses=[0]
# while True:
#     inp=int(input('enter num:'))
#     guesses.append(inp)
#     print(guesses)
#     if num-inp<num-guesses[-2]:
#         print(inp,'-closer')
#     else:
#         print(inp,'-far')

#LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even, 
# but returns the greater if one or both numbers are odd
'''
def lesser_of_two_numm(a,b):
    if (a%2 or b%2)!=0:
        print('in first if')
        return a if a>b else b
    else:
        if (a%2 and b%2)==0 and a<b:
            print('in second if')
            return a
        else:
            print('in else')
            return b
print(lesser_of_two_numm(1,6))

def lesser_of_two_num(a,b):
    if a%2==0 and b%2 ==0:
        print('in even')
        return a if a<b else b
    else:
        print('in odd case')
        return a if a>b else b

print(lesser_of_two_num(1,6))
'''

#ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter

#animal_crackers('Levelheaded Llama') --> True
#animal_crackers('Crazy Kangaroo') --> False
'''
def animal_crackers(string):
    lst=string.split(' ')
    print(lst)
    if lst[0][0]==lst[1][0]:
        return True
    else:
        return False
print(animal_crackers('Levelheaded Llama'),animal_crackers('Crazy Kangaroo'))
#sol2
def animal_crackers(text):
    wordlist = text.split()
    return wordlist[0][0] == wordlist[1][0]

print(animal_crackers('Levelheaded Llama'),animal_crackers('Crazy Kangaroo'))
'''
#MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. 
# If not, return False

# def makes_twenty(n1,n2):
#     return (n1+n2)==20 or n1==20 or n2==20
# print(makes_twenty(12,89))

#OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name

# def capitlise(word):
#     return word[0:4].capitalize()+word[4:].capitalize()
# print(capitlise('gowtham'))

# MASTER YODA: Given a sentence, return a sentence with the words reversed
# master_yoda('I am home') --> 'home am I'
# master_yoda('We are ready') --> 'ready are We'

# def master_yoda(word):
#     print(word.split(' '))
#     print(word.split(' ')[-len(word):])
#     return ' '.join(word.split(' ')[::-1])
# print(master_yoda('I am home'))
# lst=['gh','ij','kl']
# #print(lst[-1:-len(lst)-1:-1])
# print(lst[-1::-1])


# ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
# almost_there(90) --> True
# almost_there(104) --> True
# almost_there(150) --> False
# almost_there(209) --> True

# def almost_there(num):
#     return num in range(100-10,100+11) or num in range(200-10,200+11)
# print(almost_there(90),almost_there(104),almost_there(150),almost_there(191))
# def almost_there(n):
#     return ((abs(100 - n) <= 10) or (abs(200 - n) <= 10))

# print(almost_there(90),almost_there(104),almost_there(150),almost_there(191))

# FIND 33:
# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

# has_33([1, 3, 3]) → True
# has_33([1, 3, 1, 3]) → False
# has_33([3, 1, 3]) → False

# def has_33(lst):
#     for i in range(0,len(lst)-1):
#         if lst[i]==lst[i+1]:
#             return True
#     return False

# def has_33(nums):
#     for i in range(0, len(nums)-1):
      
#         # nicer looking alternative in commented code
#         #if nums[i] == 3 and nums[i+1] == 3:
    
#         if nums[i:i+2] == [3,3]:
#             return True  
    
#     return False
# print(has_33([1, 3, 3]),has_33([3, 1, 3]),has_33([1, 3, 1, 3]),has_33([1, 3, 1, 3, 3]))



# PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
# paper_doll('Hello') --> 'HHHeeellllllooo'
# paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'

# def paper_doll(word):
#     op=''
#     for i in word:
#         op+=i*3
#     return op
# print(paper_doll('Mississippi'))

# BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum.
#  If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum 
# (even after adjustment) exceeds 21, return 'BUST'
# blackjack(5,6,7) --> 18
# blackjack(9,9,9) --> 'BUST'
# blackjack(9,9,11) --> 19

# def blackjack(a,b,c):
#     if sum((a,b,c))<=21:
#         return sum((a,b,c))
#     elif sum((a,b,c))>21 and a==11 or b==11 or c==11: #elif sum((a,b,c)) <=31 and 11 in (a,b,c):
#         return sum((a,b,c))-10
#     else:
#         return 'bust'   
    
# print(blackjack(5,6,7),blackjack(9,9,9),blackjack(9,9,11))

# SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with
#  a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.
# summer_69([1, 3, 5]) --> 9
# summer_69([4, 5, 6, 7, 8, 9]) --> 9
# summer_69([2, 1, 6, 9, 11]) --> 14

# def summer_69(lst):
#     total=0
#     add=True
#     for num in lst:
#         while add:
#             if num!=6:
#                 total+=num
#                 break
#             else:
#                 add=False
#         while not add:
#             if num!=9:
#                 break
#             else:
#                 add=True
#                 break
#     return total,add
# print(summer_69([4, 5, 6, 7, 8, 9,11]))

# SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order
#  spy_game([1,2,4,0,0,7,5]) --> True
#  spy_game([1,0,2,4,0,5,7]) --> True
#  spy_game([1,7,2,0,4,5,0]) --> False

#below works only for above listed usecases

# def spy_game(lst):
#     exp=[]
#     spy=True
#     for num in lst:
#         while spy:
#             if num in(0,0,7):
#                 exp.append(num)
#                 break
#             else:
#                 break
#     return exp==[0,0,7]

# #works for majority of usecases
# def spy_game(nums):
#     code = [0,0,7,'x']
#     for num in nums:
#         if num == code[0]:
#             code.pop(0)   # code.remove(num) also works
#     return len(code) == 1
# print(spy_game([1,0,2,0,4,5,0,7,7]))

# find how many 0,0,7 are there in a list of numbers
#list=[1,0,2,0,4,6,7,0,3,0,0,7,9]---->2
'''
def find_rep(nums):
    count=0
    temp_var=[]
    for num in nums:
        if num in(0,7):
            temp_var.append(num)
            print(temp_var,count)
            if len(temp_var)>=3:
                if temp_var[2]==0:
                    temp_var.pop(2)
                    print(temp_var,count,'nknk')
            if temp_var==[0,0,7]:
                count+=1
                print(temp_var,count)
                temp_var.clear()
                print(temp_var,count)
    return temp_var,count
print(find_rep([1,0,2,0,4,6,7,0,3,0,0,7,9]))

def find_rep(nums):
    count=0
    temp_var=[]
    for num in nums:
        if num in(0,7):
            temp_var.append(num)
            if len(temp_var)>=3:
                if temp_var[2]==0:
                    temp_var.pop(2)
            if temp_var==[0,0,7]:
                count+=1
                temp_var.clear()
    return count
print(find_rep([1,0,2,0,4,6,7,0,3,0,0,7,9]))'''

#COUNT PRIMES: Write a function that returns the number of prime num that exist up to and including a given number
# num divisible by itself and one alone is prime (or) a num that is notdivisible any other num than itself(ignore 1)
# def count_primes(num):
#     prime=[]
    
#     for i in range(2,num+1):
#         count=0
#         for j in range(2,i+1):
#             if i%j==0:
#                 #  prime.append(i)
#                 count+=1
                                
#             if count==1:
#                 prime.append(i)
#                 break
    
#     return prime,count,len(prime)
# print(count_primes(100))

#Write a Python script that displays the following table
# 1 1 1 1 1
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64
# 5 1 5 25 125

# for i in range(1,6):
#     # print(i,end=' ')
#     for j in range(0,5):
#         if j==0:
#             print(i,end=' ')
#         elif j==1:
#             print(j,end=' ')
#         else:
#             print(i**(j-1),end=' ')
#     print()


# Python script to display the specified table
# for i in range(1, 6):
#     # Initialize an empty list to store each row's values
#     row_values = []
#     for j in range(5):
#         if j == 0:
#             # The first column is always the number itself (i)
#             row_values.append(str(i))
#         elif j == 1:
#             # The second column is always 1
#             row_values.append(str(1))
#         else:
#             # For the remaining columns, calculate i raised to the power of (j-1)
#             row_values.append(str(i ** (j-1)))
#     # Join the row values separated by a space and print the row
#     print(' '.join(row_values))
#     print(row_values)

# print('{1}//{0}={2}'.format(8,2,10))
# print('   Coding For All      '.strip()+str(len('Coding For All')))
# print('Coding For All'.rindex('l'))
# # print('')
# print('You cannot end a sentence with because because because is a conjunction'.replace('because ',''))

# first, second,*rest, third = [1,2,3,4,5,6,7,8,9,10]
# print(first)          # 1
# print(second)         # 2
# print(third)          # 3
# print(rest)           # [4,5,6,7,8,9]
# # print(tenth)          # 10
# countries = [
#   'Afghanistan',
#   'Albania',
#   'India',
#   'Algeria',    
#   'Andorra',
#   'Angola',
# ]
# from math import floor,ceil
# print(len(countries),floor((len(countries)/2)),list(enumerate(countries[floor((len(countries)/2))-1:ceil((len(countries)/2)+1)])))

# while True:
#     if len(countries)%2==0:
#         print('in if')
#         print(countries[len(countries)//2-1:(len(countries)//2)+1])
#         break
#     else:
#         print('in else',len(countries))
#         print(countries[len(countries)//2:(len(countries)//2)+1])
#         break
# # syntax
# st1 = {'item1', 'item2', 'item3', 'item4'}
# st2 = {'item3', 'item6', 'item7', 'item8'}
# st3 = st1.union(st2)
# print(st3)

# person = {
#     'first_name':'Asabeneh',
#     'last_name':'Yetayeh',
#     'age':250,
#     'country':'Finland',
#     'is_married':True,
#     'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
#     'address':{
#         'street':'Space street',
#         'zipcode':'02210'
#     }
#     }
# print(person.pop('first_name'))        # Removes the firstname item
# print(person.popitem())          # Removes the address item
# del person['is_married']      # Removes the is_married item
# print(person)


# def remove_item(lst,item):
#     lst.remove(item)
#     return lst
    
# food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
# print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
# numbers = [2, 3, 7, 9];
# print(remove_item(numbers, 3))  # [2, 7, 9]

# import json
# with open (r"C:\Users\vgowtham2\Documents\DSA_Python\pythonpractice\countriesdata.py",'r',encoding="utf8") as fi:
#     data=json.load(fi)
# #Create a function called the most_spoken_languages in the world. It should return 10 or 20 most spoken languages in the world in descending order
# # print(data)

# def most_spoken_lang(data):
#     all_lang=[]
#     for i in range(0,len(data)):
#         all_lang.extend(data[i]['languages'])
#     # print(all_lang)
#     count = {i: all_lang.count(i) for i in all_lang}

#     #count={}
#     # for i in all_lang:
#     #     if i not in count:
#     #         count[i]=1
#     #     else:
#     #         count[i]+=1
#     sorted_items=sorted(count.items(),key=lambda x:x[1],reverse=True)
#     # print([i[0] for i in sorted_items[:10]])
#     for i, (key, _) in enumerate(sorted_items[:10],start=1):
#         print(f"{i}. {key}")
# most_spoken_lang(data)

# #Create a function called the most_populated_countries. It should return 10 or 20 most populated countries in descending order.
# def most_populated_countries(data):
#     countries=[]
#     population=[]
#     for i in range(0,len(data)):
#         countries.append(data[i]['name'])
#         population.append(data[i]['population'])
#         # print(countries,population)
#     pop_data={k:v for k,v in zip(countries,population)}
#     sorted_data=sorted(pop_data.items(),key=lambda x:x[1],reverse=True)
#     for k,_ in sorted_data[:10]:
#         print(k)
# most_populated_countries(data)

#Write a function which check if provided variable is a valid python variable

# var=input('enter variable name:')
# import re
# def is_valid_variable(var):
#     pattern=r"^[a-zA-Z_][a-zA-Z0-9_]*$"
#     if re.match(pattern,var):
#         return True
#     else:
#         return False
    
# print(is_valid_variable("variable1"))  # True
# print(is_valid_variable("1variable"))  # False
# print(is_valid_variable("_variable"))  # True
# print(is_valid_variable("var-iable"))  # False

# ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]

# frequency = {}
# for age in ages:
#     frequency[age] = frequency.get(age, 0) + 1

# mode = max(frequency, key=frequency.get)
# # Here, frequency.get is a function that retrieves the value (frequency) associated with each key (age) in 
# # the dictionary. By specifying key=frequency.get, max() will find the key (age) with the maximum value (frequency) 
# # by comparing the values returned by frequency.get for each key
# print(mode)

# #Declare a function named user_id_gen_by_user that takes two inputs using input(). One of the inputs is the number
# #of characters and the second input is the number of IDs which are supposed to begenerated.
# import random
# import string

# def user_id_gen_by_user(uid1,num):
#     u_id=[]
#     for _ in range(uid1):
#         user_id = random.choice(string.ascii_letters)
#         user_id+=''.join(random.choices(string.ascii_letters+string.digits,k=num-1))
#         u_id.append(user_id)
#     return u_id

# uid1=int(input())
# num=int(input())
# print(user_id_gen_by_user(uid1,num))
        
        
# translation_table = str.maketrans("aeiou", "12345","cghjk")
# print(translation_table) 

# Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list

# import random
# def shuffle_list(inp):
#     op=['0']
#     for i in range(0,len(inp)):
#         if i==0 or i%2==0:
#             op.insert(i+1,inp[i])
#         else:
#             op.insert(i-1,inp[i])
#     op.remove('0')  
#     # op.insert(9,'9')
#     return op
#     # op=inp
#     # random.shuffle(op)
#     # return op

# inp=[1,2,3,4,5]
# print(shuffle_list(inp))

# import random

# def fisher_yates_shuffle(lst):
#     """
#     Shuffles the elements of the given list using the Fisher-Yates shuffle algorithm
#     and returns the shuffled list.

#     Parameters:
#         lst (list): The list to be shuffled.

#     Returns:
#         list: The shuffled list.
#     """
#     shuffled_lst = lst[:]  # Create a shallow copy of the list to avoid modifying the original list
#     n = len(shuffled_lst)
#     for i in range(n - 1, 0, -1):
#         j = random.randint(0, i)
#         shuffled_lst[i], shuffled_lst[j] = shuffled_lst[j], shuffled_lst[i]
#     return shuffled_lst

# # Example usage:
# original_list = [1, 2, 3, 4, 5]
# shuffled_list = fisher_yates_shuffle(original_list)
# print("Original List:", original_list)
# print("Shuffled List:", shuffled_list)

#Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.

# import random
# def arr_7():
#     op=set()
#     while len(op)<7:
#         # for i in range(7):
#         inp=random.randint(0,9)
#         op.add(inp)
#     return list(op)
# print(arr_7())
# print(random.sample(range(10),7))
'''-------------------------------------------------------------------------------------------'''
#Using list comprehension create the following list of tuples:
# [(0, 1, 0, 0, 0, 0, 0),
# (1, 1, 1, 1, 1, 1, 1),
# (2, 1, 2, 4, 8, 16, 32),
# (3, 1, 3, 9, 27, 81, 243),
# (4, 1, 4, 16, 64, 256, 1024),
# (5, 1, 5, 25, 125, 625, 3125),
# (6, 1, 6, 36, 216, 1296, 7776),
# (7, 1, 7, 49, 343, 2401, 16807),
# (8, 1, 8, 64, 512, 4096, 32768),
# (9, 1, 9, 81, 729, 6561, 59049),
# (10, 1, 10, 100, 1000, 10000, 100000)]

# for i in range(0,11):
#     for j in range(0,6):
        #optional lines
        # if j==0:
        #     print(i,sep=',',end=' ')
        # elif j==1:
        #     print(j,sep=',',end=' ')
        # else :
#             print(i**j,sep=',',end =' ')
#     print()   

# op=[(i,)+tuple(pow(i,j) for j in range(6)) for i in range(11)]
# print(op)

#Change the following list of lists to a list of concatenated strings:
# names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
# # output:['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']
# op=[j[0]+' '+j[1]  for i in names for j in i]
# print(op)
# Change the following list to a list of dictionaries:
# countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
# # output:
# # [{'country': 'FINLAND', 'city': 'HELSINKI'},
# # {'country': 'SWEDEN', 'city': 'STOCKHOLM'},
# # {'country': 'NORWAY', 'city': 'OSLO'}]
# op=[{'country':k.upper(),'city':v.upper()} for i in countries for k,v in i]
# print(op)
# countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
# formatted_countries = [{'country': country.upper(), 'city': city.upper()} for sublist in countries for country, city in sublist]
# print('[', end='')
# for country_info in formatted_countries:
#     print(country_info, end='')
#     if country_info != formatted_countries[-1]:
#         print(',')
#     else:
#         print(']')

#flatten the list
#countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
# output:[['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]

# op=[['{}, {}, {}'.format(i.upper(),i[:3].upper(),j.upper()) for i,j in sub_list] for sub_list in countries ]
# print(op)

# count=0
# for i in countries:
#     print(i)
#     for j,k in i:
#         count+=1
#         print(j,k,count)
        
'''---------------------------------------------------------------------------------------------------------------'''
# print((1,)+(1,3,(92,3)))
# a=(1,)
# print(a,id(a))
# a=a+(2,3)
# print(a,id(a))
# a=[1]
# print(a,id(a))
# a.append(2)
# print(a,id(a))

#####################################-----------Decorators-----------#####################################
# def my_decorator(func):
#     def wrapper():
#         print("Something is happening before the function is called.")
#         # func()
#         print("Something is happening after the function is called.")
#     return wrapper

# @my_decorator
# def say_hello():
#     print("Hello!")

# say_hello()

# def decorator(func):
#     print("Decorator setup")

#     # Define a wrapper function
#     def wrapper(*args, **kwargs):
#         print("Wrapper setup")
#         # Call the original function
#         result = func(*args, **kwargs)
#         print("Wrapper teardown")
#         return result

#     # Perform some additional setup here if needed

#     # Return None
#     return None

# @decorator
# def my_function():
#     print("Original function")

# # Call the decorated function
# my_function()

# def sumd(func):
#     print('in dec funnc')
#     def inn():
#         print('in inner func')
#         func()
#     return inn
# # @sumd 
# def start():
#     print('process end')
# print(start)
# start=sumd(start)
# start()


# '''These decorator functions are higher order functions
# that take functions as parameters'''

# # First Decorator
# def uppercase_decorator(function):
#     print('dec upper')
#     def wrapper():
#         print('upper.wrap')
#         func = function()
#         make_uppercase = func.upper()
#         return make_uppercase
#     return wrapper

# # Second decorator
# def split_string_decorator(function):
#     print('dec split')
#     def wrapper():
#         print('split.wrap')
#         func = function()
#         splitted_string = func.split()
#         return splitted_string

#     return wrapper

# # @split_string_decorator
# # @uppercase_decorator     # order with decorators is important in this case - .upper() function does not work with lists
# def greeting():
#     return 'Welcome to Python'
# # greeting=uppercase_decorator(greeting) 
# # uppercase_decorator=split_string_decorator(uppercase_decorator)
# # greeting = split_string_decorator(uppercase_decorator(greeting))
# '''The split_string_decorator function takes the result of uppercase_decorator(greeting) as its argument. 
# This result is the wrapper function created within the uppercase_decorator function. Therefore, the wrapper
# function returned by uppercase_decorator is passed as an argument to split_string_decorator.
# So, in this scenario, the wrapper function of the split_string_decorator contains a reference to the wrapper 
# function of the uppercase_decorator. When you call greeting, both wrapper functions are executed in sequence 
# due to the decorator chaining.'''

# print(greeting())   # WELCOME TO PYTHON

'''1.  # First Decorator
2.  def uppercase_decorator(function):
3.      def wrapper():
4.          func = function()  # Here, 'function' is 'greeting', so 'func' becomes 'Welcome to Python'
5.          make_uppercase = func.upper()  # 'make_uppercase' becomes 'WELCOME TO PYTHON'
6.          return make_uppercase  # Returns 'WELCOME TO PYTHON'
7.
8.  # Second decorator
9.  def split_string_decorator(function):
10.     def wrapper():
11.         func = function()  # Here, 'function' is the inner function returned by 'uppercase_decorator',
12.                            # so 'func' becomes 'WELCOME TO PYTHON'
13.         splitted_string = func.split()  # 'splitted_string' becomes ['WELCOME', 'TO', 'PYTHON']
14.         return splitted_string  # Returns ['WELCOME', 'TO', 'PYTHON']
15.
16. # Define the function to be decorated
17. def greeting():
18.     return 'Welcome to Python'
19.
20. # Apply the decorators manually
21. greeting = split_string_decorator(uppercase_decorator(greeting))  # Line 21 starts executing here
22. # 'uppercase_decorator(greeting)' returns the 'wrapper' function
23. # 'split_string_decorator(wrapper)' returns the 'wrapper' function
24.
25. print(greeting())   # Output: ['WELCOME', 'TO', 'PYTHON']
'''
# from itertools import zip_longest
# numbers = [1, 2, 3, 4, 5] # iterable
# def square(x):
#     return x ** 2
# numbers_squared = map(square, numbers)
# key=['a','b','c','d']
# # print(dict(zip(key,list(numbers_squared))))   # [1, 4, 9, 16, 25]
# print(dict(zip_longest(key,numbers,fillvalue='NEW')))
# # Lets apply it with a lambda function
# numbers_squared = map(lambda x : x ** 2, numbers)
# print(list(numbers_squared))    # [1, 4, 9, 16, 25]
# class Nubers:
#     @classmethod
#     def numbers(cls):
#         pass
# print(isinstance(Nubers.numbers,classmethod))
# class Numbers:
#     @classmethod
#     def numbers(cls):
#         pass

# print(isinstance(Numbers.numbers, classmethod))

# a=[1,2]
# print(id(a.__add__([3,4,1,2])))
# print(a,id(a))
# a.append([1,2])
# print(a,id(a))
# a=[1,2]
# b=[3,4]
# print(id(a),id(a+b))
# from collections import OrderedDict

# a = {}
# for i, j in [(2, 3), (4, 5)]:
#     # print(i, j)
#     if i not in a:  # Check if the key i is not already in the dictionary
#         a[i] = OrderedDict()
#     a[i][j] = j  # Add j as a key in the OrderedDict associated with key i
# print(a)

# from collections import OrderedDict
# a={}
# for i,j in [(2,3),(4,5)]:
#     # print(i,j)
#     a[i]=OrderedDict([(j,i)])
# print(a,list(a.items()))


#-----------------------------| LAMBDA | MAP | FILTER | REDUCE| -------------------------
# countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
# names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Use map to create a new list by changing each country to uppercase in the countries list
'''def UC_countries(country):
    uc=country.upper()
    return uc

op=map(UC_countries,countries)
print(list(op))'''

# Use map to create a new list by changing each number to its square in the numbers list
'''def sq_num(x):
    return(x**2)

op=map(sq_num,numbers)
print(list(op))'''
# Use filter to filter out countries containing 'land'.     
'''def rem(name):
    if 'land' in name:
        return name
    # else: 
        
op=filter(rem,countries)
print(tuple(op))'''
# Use filter to filter out countries having exactly six characters.

'''def fc(country):
    if len(country)>=6: # country.startswith('E'):
        return country
print(list(filter(fc,countries)))'''

# Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.

"""def get_str_lst(inp):
    op=[]
    for i in range(0,len(inp)):
        if type(inp[i])==str:
            op.append(inp[i])
    return op

print(get_str_lst([1,2,'3','4']))"""

# Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))
# from functional import seq
# from collections import namedtuple

# Transaction = namedtuple('Transaction', ['reason','amount'])
# transactions = [
#     Transaction('github', 7),
#     Transaction('food', 10),
#     Transaction('coffee', 5),
#     Transaction('digitalocean', 5),
#     Transaction('food', 5),
#     Transaction('riotgames', 25),
#     Transaction('food', 10),
#     Transaction('amazon', 200),
#     Transaction('paycheck', -1000)
# ]

# # Using the Scala/Spark inspired APIs
# food_cost = seq(transactions)\
#     .filter(lambda x: x.reason == 'food')\
#     .map(lambda x: x.amount).sum()
# print(food_cost)
# # Using the LINQ inspired APIs
# food_cost = seq(transactions)\
#     .where(lambda x: x.reason == 'coffee')\
#     .select(lambda x: x.amount).sum()
# print(food_cost)
# # Using PyFunctional with fn
# from fn import _
# food_cost = seq(transactions).filter(_.reason == 'food').map(_.amount).sum()
# print(food_cost)

# # m = itertools.imap
# # f = itertools.ifilter
# # def final_map_fn(item):
# #    if (item.type == "cake"):
# #         catalog_item = retrieve_catalog_item(item.id);
# #         return {
# #             "id": item.id,
# #             "weight": item.weight,
# #             "barcode": catalog_item.barcode}
# #     else:
# #         return default_transformer(item)

# # items = m(as_item,shop.inventory) #note it does not loop it yet
# # instockitems = f(is_in_stock,items) #still hasnt actually looped anything
# # weighteditems = (item for item instockitems if item.weight < 100) #still no loop (this is a generator)
# # final_items = m(final_map_fn,weighteditems) #still has not looped over a single item in the list
# # results = list(final_items) #evaluated now with a single loop

# Use reduce to sum all the numbers in the numbers list.
# Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries

# from functools import reduce
# def con_co(x,y):
#     if y!=countries[-1]:
#         return x+', '+y
#     else:
#         return x+' and '+y

# # op=reduce(lambda x,y: x+', '+y if y != countries[-1] else x+' and '+y,countries)
# # print(op+' are NA countries')
# # countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
# op=reduce(con_co,countries)
# print(op+' are NA countries')
# Declare a function called categorize_countries that returns a list of countries with some common pattern (you can find the countries list in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')).
'''countries = [
  'Afghanistan',  'Albania',  'Algeria',  'Andorra', 'Angola',  'Antigua and Barbuda',  'Argentina',
  'Armenia',  'Australia',  'Austria',  'Azerbaijan',  'Bahamas',  'Bahrain',  'Bangladesh',  'Barbados',
  'Belarus',  'Belgium',  'Belize',  'Benin',  'Bhutan',  'Bolivia',  'Bosnia and Herzegovina',  'Botswana',
  'Brazil',  'Brunei',  'Bulgaria',  'Burkina Faso',  'Burundi',  'Cambodia',  'Cameroon',  'Canada',  'Cape Verde',
  'Central African Republic',  'Chad',  'Chile',  'China',  'Colombi',  'Comoros',  'Congo (Brazzaville)',  'Congo',
  'Costa Rica',  "Cote d'Ivoire",  'Croatia',  'Cuba',  'Cyprus',  'Czech Republic',  'Denmark',  'Djibouti',  'Dominica',
  'Dominican Republic',  'East Timor (Timor Timur)',  'Ecuador',  'Egypt',  'El Salvador',  'Equatorial Guinea',
  'Eritrea',  'Estonia',  'Ethiopia',  'Fiji',  'Finland',  'France',  'Gabon',  'Gambia, The',  'Georgia',  'Germany',
  'Ghana',  'Greece',  'Grenada',  'Guatemala',  'Guinea',  'Guinea-Bissau',  'Guyana',  'Haiti',  'Honduras',
  'Hungary',  'Iceland',  'India',  'Indonesia',  'Iran',  'Iraq',  'Ireland',  'Israel',  'Italy',  'Jamaica',  'Japan',
  'Jordan',  'Kazakhstan',  'Kenya',  'Kiribati', 'Korea, North',  'Korea, South',  'Kuwait',  'Kyrgyzstan',  'Laos',
  'Latvia',  'Lebanon',  'Lesotho',  'Liberia',  'Libya',  'Liechtenstein',  'Lithuania',  'Luxembourg',  'Macedonia',
  'Madagascar',  'Malawi',  'Malaysia',  'Maldives',  'Mali',  'Malta',  'Marshall Islands',  'Mauritania',  'Mauritius',
  'Mexico',  'Micronesia',  'Moldova',  'Monaco',  'Mongolia',  'Morocco',  'Mozambique',  'Myanmar',  'Namibia',  'Nauru',
  'Nepal', 'Netherlands', 'New Zealand',  'Nicaragua',  'Niger',  'Nigeria',  'Norway',  'Oman',  'Pakistan',  'Palau',
  'Panama','Papua New Guinea',  'Paraguay',  'Peru',  'Philippines',  'Poland',  'Portugal',  'Qatar',  'Romania',
  'Russia',  'Rwanda', 'Saint Kitts and Nevis', 'Saint Lucia',  'Saint Vincent',  'Samoa',  'San Marino',  'Sao Toe and Principe',
  'Saudi Arabia',  'Senegal', 'Serbia and Montenegro',  'Seychelles',  'Sierra Leone',  'Singapore',  'Slovakia',
  'Slovenia',  'Solomon Islands',  'Somalia', 'South Africa', 'Spain', 'Sri Lanka',  'Sudan',  'Suriname',  'Swaziland',
  'Sweden',  'Switzerland',  'Syria',  'Taiwan',  'Tajikistan',  'Tanzania',  'Thailand',  'Togo',  'Tonga',  'Trinidad and Tobago',
  'Tunisia',  'Turkey',  'Turkmenistan',  'Tuvalu',  'Uganda',  'Ukraine',  'United Arab Emirates',  'United Kingdom',
  'United States',  'Uruguay',  'Uzbekistan',  'Vanuatu',  'Vatican City',  'Venezuela',  'Vietnam',  'Yemen',  'Zambia',
  'Zimbabwe',]'''
#  Declare a function called categorize_countries that returns a list of countries with some common pattern (you can find the countries list in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')).
# def categorize_countries(coun3tries):
#     stan=[]

#     land=[]
#     ia=[]
#     other=[]
#     for i in countries :
#         if 'stan' in i:
#             stan.append(i)
#         elif 'ia' in i:
#             ia.append(i)
#         elif 'land' in i:
#             land.append(i)
#         else:
#             other.append(i)
#     yield stan,ia,land,other

# print(categorize_countries(countries))
# Create a function returning a dictionary, where keys stand for starting letters of countries and values are the number of country names starting with that letter.
# a={'1':'a','2':'b'}
# print('1' in a)
# def k_v(countries):
#     count={}
#     for i in countries:
#         key=i[0]
#         if i[0] in count:
#             count[key]+=1#count[key].append(i)
#         else:
#             count.update({i[0]:1})#count.update({str(i[0]):[i]})
#     return count

# op=k_v(countries)
# print(op)

# Declare a get_first_ten_countries function - it returns a list of first ten countries from the countries.js list in the data folder.
# Declare a get_last_ten_countries function that returns the last ten countries in the countries list.
# Use the countries_data.py (https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py) file and follow the tasks below:
# import json
# with open (r"C:\Users\vgowtham2\Documents\DSA_Python\pythonpractice\countriesdata.py",'r',encoding="utf8") as fi:
#     data=json.load(fi)
#     # print(data)
#     # Sort countries by name, by capital, by population
# # def sortby_nm_cap_pop(data):
# new_list=sorted(data,key=lambda key:(key['name'],key['capital']),reverse=True)
# print(new_list)

# Sort out the ten most spoken languages by location.
"""with open('useful_func','w') as f:
    f.write('''def get_10(data):
    sorted_data=sorted(data,key=lambda key:key['population'],reverse=True)
    count=0
    for i in sorted_data:
        count+=1
        if count==10:
            break
        print(i['name'])''')"""

# from useful_func import top_10 
# from useful_func import get_10
# '''opp=get_10(data)
# # print(opp)

# with open(r'C:\Users\vgowtham2\Documents\DSA_Python\pythonpractice\op_useful_func','a') as op:
#     for i in opp:
#         op.write(i+'\n')'''
# Sort out the ten most populated countries.
# print(get_10(data))

# from datetime import datetime
# now = datetime.now()
# print(now)                      # 2021-07-08 07:34:46.549883
# day = now.day                   # 8
# month = now.month               # 7
# year = now.year                 # 2021
# hour = now.hour                 # 7
# minute = now.minute             # 38
# second = now.second
# timestamp = now.timestamp()
# # print(day, month, year, hour, minute)
# print('timestamp', timestamp)
# print(f'{day}/{month}/{year}, {hour}:{minute}')  # 8/7/2021, 7:38

# t1 = datetime(year = 1999, month = 10, day = 18)
# t2 = datetime(year = 2024, month = 4, day = 9)
# diff = t2 - t1
# print(diff.days/365)
# Today is 5 December, 2019. Change this time string to time.
'''from datetime import datetime,timedelta
now='5 DECEMBER 2019'
str_time=datetime.strptime(now,'%d %B %Y')
print(str_time)
now=datetime.now()
op=now.strftime('%B-%d-%Y')
print(op)
new_year=datetime(day=1,month=1,year=2025)
t1=timedelta(new_year)
t2=timedelta(now)
print(t1-t2)'''
'''try:
    name = input('Enter your name:')
    year_born = input('Year you born:')
    age = 2019 - int(year_born)
    print('You are {name}. And your age is {age}'.format(name=name,age=age))
except Exception as e:
    print(e)'''

# today=datetime.now()
# # dob=datetime.date(2024)
# print(today.date(),type(today.date()))

# def unpacking_person_info(name, country, city, age):
#     return f'{name} lives in {country}, {city}. He is {age} year old.'
# dct = {'name':'Asabeneh', 'country':'Finland', 'city':'Helsinki', 'age':250}
# print(unpacking_person_info(**dct)) # Asabeneh lives in Finland, Helsinki. He is 250 years old.

# #Unpack the first five countries and store them in a variable nordic_countries, store Estonia and Russia in es, and ru respectively.
# names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']
# *ff,es,ru=names
# print("grouped list{ff}, separate {es}{ru}".format(ff=ff,es=es,ru=ru))

# import re

# txt = '''Python is the most beautiful language that a human being has ever created.
# I recommend python for a first programming language'''

# # It returns an object with span and match
# match = re.search('first', txt, re.I)
# print(match)  # <re.Match object; span=(100, 105), match='first'>
# # We can get the starting and ending position of the match as tuple using span
# span = match.span()
# print(span)     # (100, 105)
# # Lets find the start and stop position from the span
# start, end = span
# print(start, end)  # 100 105
# substring = txt[start:end]
# print(substring)       # first

# match=re.match('python',txt,re.I)
# print(match)

# txt = '''Python is the most beautiful language that a human being has ever created.
# I recommend python for a first programming language'''

# # It return a list
# matches = re.findall('language', txt, re.I)
# print(matches)  # ['language', 'language']

# txt='dove is a bird'
# regex=r'[a-z]+'
# match=re.findall(regex,txt)
# print(match)

# regex_pattern = r'[a].'  # this square bracket means a and . means any character except new line
#txt = '''Apple and banana are fruits'''

# idx=0
# matches = re.search(regex_pattern, txt)
# for i in txt:
#     print(matches,matches.span()[1],type(matches.span()[1]))
#     matches = re.search(regex_pattern, txt[matches.span()[1]])# ['an', 'an', 'an', 'a ', 'ar']
#     # idx=matches.span()[1]
#     # print(matches,matches.span()[1])

#regex_pattern = r'[a].{3}'  # . any character, + any character one or more times 
#matches = re.findall(regex_pattern, txt)
# print(matches)  # ['and banana are fruits']

'''paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'

reg_ex=r'[a-z]+'
matches=re.findall(reg_ex,paragraph,re.I)
# print(matches)
op={}
for i in matches:
    if i not in op:
        op[i]=1
    else:
        op[i]+=1
# print(op)
op1=[(value,key) for key,value in op.items()]
print(sorted(op1,reverse=True))'''
#paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'

# reg_ex=r'[a-z]+'
# matches=re.findall(reg_ex,paragraph,re.I)
# print(matches)
# op={}
# for i in matches:
#     if i not in op:
#         op[i]=1
#     else:
#         op[i]+=1
# # print(op)
# op1=[(value,key) for key,value in op.items()]
# print(sorted(op1,reverse=True))

# txt='''The position of some particles on the horizontal x-axis are-120-2222 -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8, 5 in the 
#  positive direction. Extract these numbers from this whole text and find the distance between the two furthest particles.'''

# regex_pattern=r'-?\d{1,4}'
# matches=re.findall(regex_pattern,txt)
# srtd_lst1=[int(i) for i in matches]   
# srtd_lst=sorted(srtd_lst1)
# print(srtd_lst)
# db=int(srtd_lst[-1])+abs(int(srtd_lst[0]))
# print(db,int(srtd_lst[-1]),abs(int(srtd_lst[0])))

# def is_valid_variable(val):
#     reg_exp=r'^[a-zA-Z_]+[^-]{1,10}\w+'
#     matches=re.match(reg_exp,val)
#     # print(matches.group(),val)
#     try:
#         print(matches.group()==val)
#     except AttributeError:
#         print('False')

# is_valid_variable('first_name') # True
# is_valid_variable('first-name') # False
# is_valid_variable('1first_name') # False
# is_valid_variable('firstname') # True

# Clean the following text. After cleaning, count three most frequent words in the string.
# sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''
# def clean_text(txt):
#     reg_ex=r'[%*&$#@!();.?,]+'
#     matches=re.sub(reg_ex,'',txt)
#     return matches
# cleaned_text=clean_text(sentence)
# print(cleaned_text)
# #I am a teacher and I love teaching There is nothing as more rewarding as educating and empowering people I found teaching more interesting than any other jobs Does this motivate you to be a teacher
# def most_frequent_words(inp):
#     dict={}
#     for i in inp.split():
#         if i not in dict:
#             dict[i]=1
#         else:
#             dict[i]+=1
#     op=[(val,key) for key,val in dict.items()]
#     sorted_it=sorted(op,reverse=True)
#     return sorted_it[:3]

# print(most_frequent_words(clean_text(sentence))) # [(3, 'I'), (2, 'teaching'), (2, 'teacher')] 
                           
# with open(r'C:\Users\vgowtham2\Documents\DSA_Python\test.txt','w') as f:
#     f.write('This text will be written in a newly created file')
                                                                                                       
# import os
# os.remove(r'C:\Users\vgowtham2\Documents\DSA_Python\test.txt')

#Write a function which count number of lines and number of words in a text. All the files are in the data the folder:
# with open(r'C:\Users\vgowtham2\Documents\DSA_Python\speech.txt','r') as f:
    # inp=f.read()
    # # Split_text=f.read().split()
    # # joined_txt=' '.join(Split_text)
    # # final_data=joined_txt.split(' ')
    # # print(final_data)
    # final_data=' '.join([str(i) for i in f.read().split()])
    # print(final_data)
    # reg_ex=r'\w+|[.,;\']'
    # matches=re.findall(reg_ex,inp)
    # reg_ex=r'(\b\w+|b)|\n'
    # reg_ex='\w+|[\n.,;]'
    # matches=re.findall(reg_ex,inp)
    # print(matches)  
    
#_-------------------------------------------------Pandas------------------------------------------------------

# import pandas as pd # importing pandas as pd
# import numpy  as np # importing numpy as np

# nums = [1, 2, 3, 4,5]
# s = pd.Series(nums,index=[2,3,4,5,9])
# print(s)
    
# dct = {'name':'Asabeneh','country':'Finland','city':'Helsinki'}
# s = pd.Series(dct)
# print(s)

# s = pd.Series(np.linspace(5, 20, 10)) # linspace(starting, end, items)
# print(s)

# data = [
#     ['Asabeneh', 'Finland', 'Helsink'], 
#     ['David', 'UK', 'London'],
#     ['John', 'Sweden', 'Stockholm']
# ]
# df = pd.DataFrame(data, columns=['Names','Country','City'])
# print(df)

# data = {'Name': ['Asabeneh', 'David', 'John'], 'Country':[
#     'Finland', 'UK', 'Sweden'], 'City': ['Helsiki', 'London', 'Stockholm']}
# df = pd.DataFrame(data)
# print(df)


#df = pd.read_csv('weight-height.csv')
# print(df)
# print(df.head(),df.tail(6),df.shape, sep='\n')
# print(df['Height'])
# print(df['Height'].describe(),df.describe()) # give statisical information about height data
    
# df['Height'] = df['Height'] * 0.01
# Using functions makes our code clean, but you can calculate the bmi without one
# def calculate_bmi ():
#     weights = df['Weight']
#     heights = df['Height']
#     bmi = []
#     for w,h in zip(weights, heights):
#         b = w/(h*h)
#         bmi.append(b)
#     return bmi
    
# bmi = calculate_bmi()
# print(bmi)
# df['BMI']=bmi
# print(df.head())
# from datetime import datetime
# yr=datetime.now().year
# print(type(yr),yr)
# print(df.Weight.dtype)
# print(pd.Series(10,index=[0,9]))
# print(pd.Series(np.linspace(6,10,5)))

# import numpy as np
# from array import *

# # a=np.array([1,2,3,4,5])
# # for i in range(0,5):
# #     print(id(a[i]))
    
# a=array('i',[1,2,3,45,55,5,6])
    
# a=[[1,2],[3,4],[5,6,5]]
# print(a)
# b=np.insert(a,2,[[7,8]],axis=0)
# print(b)

# lst=[]
# while True:
#     inp=input('enter a num:')
#     if inp=='done': break
#     lst.append(float(inp))
# print(sum(lst)/len(lst))
# from copy import copy
# a=[2,1,74,5,6]
# orig=copy(a)
# a.sort()
# print(orig,a)

## Enter num of days temp to be recorded then find it's average and display how many days temp is high than avg.

# days=int(input('Enter number of days:'))
# temp_lst=[]
# for i in range(days):
#     temp=float(input('Enter temp:'))
#     temp_lst.append(temp)
# print(temp_lst)
# avg_temp=sum(temp_lst)/len(temp_lst)
# print('Avg temparature: ',sum(temp_lst)/len(temp_lst))
# temp_lst.sort()
# print(temp_lst)
# count=0
# for idx,value in enumerate(temp_lst):
#     if value>avg_temp:
#         count+=1
# print(count,'day(s) temp more than avg temp')

#missing number
# def missing_number(arr, n):
#     # TODO
#     for i in range(0,n-1):
#         if arr[i]+1==arr[i+1]:
#             pass
#         else:
#             print(arr[i]+1)
# arr=[1,2,3,4,5,7,8,10,11,14]
# n=len(arr)
# missing_number(arr,n)

# def missing_number(arr, n):
#     # Calculate the sum of first n natural numbers
#     total = n * (n + 1) // 2
#     # Calculate the sum of numbers in the array
#     sum_arr = sum(arr)
#     # Find the missing number by subtracting sum_arr from total
#     missing = total - sum_arr
#     return missing
# # Example
# print(missing_number([1, 2, 3, 4, 6], 6))  # Output: 5
    
    
# def roman_to_integer(roman):
#     # Define a dictionary to map Roman numerals to integer values
#     roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    
#     # Initialize the result variable to store the integer value
#     result = 0
    
#     # Iterate through the Roman numeral string
#     for i in range(len(roman)):
#         # If the current numeral is smaller than the next numeral, subtract its value
#         if i < len(roman) - 1 and roman_numerals[roman[i]] < roman_numerals[roman[i + 1]]:
#             result -= roman_numerals[roman[i]]
#         # Otherwise, add its value to the result
#         else:
#             result += roman_numerals[roman[i]]
    
#     return result

# # Test the function with a Roman numeral
# roman_numeral = 'MCMLIV'  # Example: 1954
# integer_number = roman_to_integer(roman_numeral)
# print(f"The integer value of the Roman numeral '{roman_numeral}' is: {integer_number}")

## CQ Two sum , find the elements in the given array that sums up to the target number.
#a=[1,3,2,2,3,4,5]
#targ=4
# for i in range(0,len(a)):
#     for j in range(i+1,len(a)):
#         if a[i]==a[j]:
#             print(i,j,'i')
#             continue
#         elif a[i]+a[j]==targ:
#             print(i,j)
# a=[1,3,2,2,3,4,5]
# targ=4   
# pair=[]
# for idx,nums in enumerate(range(0,len(a))):
#     tgt=targ
#     tgt=tgt-a[nums]
#     if tgt in a and [tgt,a[nums]] not in pair:
#         pair.append([a[nums],tgt])
#         print('pair:',pair)
#         print(a.index(a[nums]),a.index(tgt))
# print(pair)
    
# arr = [1, 7, 3, 4, 9, 5] 
# max1,max2=0,0
# def max_product(arr):
#     global max1,max2
#     for num in arr:
#         if num>max1:
#             max2=max1
#             max1=num
#         elif num>max2:
#             max2=num
#     return max1*max2    
# print(max_product(arr)) # Output: 63 (9*7)

# def middle(lst):
#     mlst=[]
#     mlst.extend(lst[1:len(lst)])
#     print(mlst)
#     mlst.pop(-1)
#     return mlst
# myList = [1, 2, 3, 4]
# print(middle(myList))  # [2,3]

# def diagonal_sum(matrix):
#     # TODO
#     op=0
#     for i in range(0,len(myList2D)):
#         for j in range(0,len(myList2D)):
#             if i==j:
#                 op+=myList2D[i][j]
#     return op

# myList2D= [[1,2,3],[4,5,6],[7,8,9]] 
# print(diagonal_sum(myList2D)) # 15

# import copy
# def pair_sum(myList, sum):
#     op=[]
#     dup_list=copy.copy(myList)
#     for i in dup_list:
#         for j in myList:
#             if i+j==sum: 
#                 print(i,j)
#                 op.extend([str(i)+'+'+str(j)])
#                 print(op)
#                 print(myList)
#                 # myList.remove(i)
#                 myList.remove(j)
#                 print(myList)
#                 break
#     return op
# pair_sum([2, 4, 3, 5, 6, -2, 4, 7, 8, 9],7)
    
    
# def pair_sum(myList, sum):
#     op=[]
#     for i in range(0,len(myList)):
#         for j in range(i+1,len(myList)):
#             if myList[i]+myList[j]==sum:
#                 if not any (f"{myList[i]}+{myList[j]}" in op or f"{myList[i]}+{myList[j]}" in op for op in op): 
#                     op.append(f"{myList[i]}+{myList[j]}")
#     return op
# print(pair_sum([2, 4, 3, 5, 6, -2, 4, 7, 8, 9],7))
    
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

    
# rotate a matrix,

# def rotate(matrix):
#     n = len(matrix)
 
#     # Transpose the matrix
#     for i in range(n):  # Iterate over the rows
#         for j in range(i, n):  # Iterate over the columns starting from the current row 'i'
#             # Swap the elements at positions (i, j) and (j, i)
#             print(i,'=',matrix[i],'|||',j,'=',matrix[j])
#             print(f"{i}={matrix[i]}|||{j}={matrix[j]}")
#             matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
 
#     # Reverse each row
#     for row in matrix:  # Iterate over each row in the matrix
#         row.reverse()  # Reverse the elements in the current row
    
# print(rotate([[1,2,3],[4,5,6],[7,8,9]]))
    
    
# def rotate(matrix):

#     transpose_matrix=list(zip(*matrix))
#     print(matrix,'\n',transpose_matrix)
    
# print(rotate([[1,2,3],[4,5,6],[7,8,9]]))
    

# def merge_dicts(dict1, dict2):
#     # TODO
#     #dict1.update(dict2)
#     #res = {**dict1, **dict2}
#     # res = dict1 | dict2
#     for i in dict2:
        
#         if i in dict1:
#             dict1[i]+=dict2[i]
#             # print(dict1)
#             print(i,dict1[i])
#         else:
#             dict1[i]=dict2[i]
#             # dict1.update({dict1[i]=dict2[i]})
#     print(dict1)
    
# dict1 = {'a': 1, 'b': 2, 'c': 3}
# dict2 = {'b': 318, 'c': 4, 'd': 555, 'a':99}
# print(sorted(dict2.values()))
# op=dict2.update({'f':33})
# op1=dict2
# print(merge_dicts(dict1, dict2))
# op={k:v for k,v in dict2.items() if v>100}
# print(op,dict2,op1)
#reverse a list

# arr=[1,2,3,4,5,6,7]
# # b=[]
# # arr=[]
# for i in range(0,int(len(arr)/2)):
#     oth=len(arr)-i-1
#     st=arr[i]
#     # print(arr)
#     arr[i]=arr[oth]
#     arr[oth]=st
# print(arr)

# def max_value_key1(my_dict):
#     # TODO
#     key=''
#     value=0
#     for k,v in my_dict.items():
#         if v>value:
#             value=v
#             key=k
#         else:
#             continue
#     return key #return max(my_dict, key=my_dict.get)
# value=0
# def getop(val):
#     # print(val,type(val))
#     return my_dict[val]
# def max_value_key(my_dict):
#     return max(my_dict, key=getop)
# my_dict = {'a': 5, 'b': 9, 'c': 2}
# print(max_value_key(my_dict))
# string_list = ["Geeks", "for", "Geeks"]

# def len1(a):
#     return len(a)
# max_val = max(string_list, key=len1)
# print(max_val)

# def check_same_frequency(list1, list2):
#     # TODO
#     d1={}
#     d2={}
#     for i in list1:
#         d1[i]=d1.get(i,0)+1
#     for i in list2:
#         d2[i]=d2.get(i,0)+1
#     print(d1,d2)
#     print(sorted(d1.values()),sorted(d2.values()))
#     # return sorted(d1.values())==sorted(d2.values())
#     # return d1==d2
# list1 = [1, 2, 3, 2, 1]
# list2 = [3, 1, 2, 1, 2]
# print(check_same_frequency(list1, list2))

#using recursion
# def check_same_frequency(list1, list2):
#     def count_elements(lst):
#         counter = {}
#         for element in lst:
#             counter[element] = counter.get(element, 0) + 1
#         return counter
    
#     return count_elements(list1) == count_elements(list2)
# list1 = [1, 2, 3, 2, 1]
# list2 = [3, 1, 2, 1, 2]
# print(check_same_frequency(list1, list2))

# def tuple_elementwise_sum(tuple1, tuple2):
#     print(list(zip(tuple1, tuple2)))
#     return tuple(map(sum, zip(tuple1, tuple2)))

# tuple1 = (1, 2, 3)
# tuple2 = (4, 5, 6)
# output_tuple = tuple_elementwise_sum(tuple1, tuple2)
# print(output_tuple) 


# Reverse an array

arr=[1,2,3,4,5]
for i in range(len(arr)):
    idx=i-len(arr)
    