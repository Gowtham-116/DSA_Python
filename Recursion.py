#Recursion(recursive functions) stores all its previous calls in stack memory and hence prints
# or executes values in LIFO order


# def firstmethod():
#     secondmethod()
#     print("In first method")
# def secondmethod():
#     thirdmethod()
#     print("In second method")
# def thirdmethod():
#     fourthmethod()
#     print("In third method")
# def fourthmethod():
#     print('In fourth method')
# firstmethod()

#print numbers in ascending order using recursion
# def num(n):
#     if n<=10:
#         num(n+1)
#         print(n)
        
#     else:
#         print('num >10')
# num(1)


#Print numbers in descending order
# def num(n):
#     if n<1:
#         print('num<1')  
#     else:
#         print(n)
#         num(n-1)
# num(10)


#factorial of number
# n=int(input('enter num:'))
# def fact(n):
#     assert n>=0 and int(n)==n, 'The number must be positive integer only'
#     if n in [0,1]:
#         return 1
#     else:
#         return n*fact(n-1)  
# print(fact(n))


# Fibonacci numbers(0,1,1,2,3,5,8,13,21,34,55,89,.....) using recursion

# def fib(n):
#     if n in [0,1]:
#         return n
#     else:
#         return fib(n-1)+fib(n-2)
# n=10
# n=n+1
# print(fib(n))

# Using iteration

# a=0
# fn=0
# b=1
# for i in range(1,10):
#     fn=a+b
#     a=b
#     b=fn
# print(fn)

#Sum of digits of a number using recursion
# f(n)= n%10+f(n/10)

'''num=456
def sumofdigits(num):
    if num==0:
        return 0
    else:
        return num%10+sumofdigits(num//10)
        #return int(num%10)+int(sumofdigits(num/10))
print(sumofdigits(num))'''

#calculate power of a number using recursion
#Xpow(n) = n * Xpow(n-1)

'''def power(base,exp):
    assert exp>=0 and int(exp)==exp, "The exp should be positive integer only"
    if exp==0:
        return 1
    if exp==1:
        return base
    return base*power(base,exp-1)
print(power(-4,5))'''

#product of array
'''arr=[1,2,3,4]
def productOfArray(arr):
    if len(arr) == 0:
        return 1
    return arr[0] * productOfArray(arr[1:])
print(productOfArray(arr))'''

# def multiply(a, b):
#     return a * b
# x = multiply(3, 4)
# print(x)

# def return_sum(x = 1, y = 2):
#     return x + y
# # print(return_sum)
# print(return_sum (y = 2))

# a=0.1+0.2-0.3
# b=0.0
# print(a-b)
# print('yes' if a==b else 'no')