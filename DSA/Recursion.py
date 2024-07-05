# Find sum of digits of a positive integer number using recursion.
# Num:10==>1,0=>1+0=>1

# def SumOfDigits(n):
#     assert n>=0 and int(n)==n, 'Number should be positive integer'
#     if n==0:
#         return 0
#     else:
#         return int(n%10)+SumOfDigits(n//10)
# print(SumOfDigits(891019))  

# Find power of a number using recursion.
import sys
sys.setrecursionlimit(90000)

# def power(n,pow):
#     if pow==0:
#         return 1
#     if pow==1:
#         return n
#     else:
#         return n*power(n,pow-1)
    
# print(power(10,300))

# Exponentiation by squaring
# def power(n,pow):
#     assert (n>=0 and pow>=0) and int(pow)==pow , 'non valid values given'
#     if pow==0:
#         print('if')
#         return 1
#     elif pow%2==0:
#         print('elif')
#         half_pow=power(n,pow//2)
#         return half_pow*half_pow
#     else:
#         print('else')
#         return n*power(n,pow-1)
    
# print(power(10,10))

#GCD of numbers

# def gcd(a,b):
#     if b==0:
#         return a
#     else:
#         # rem=a%b
#         return gcd(b,a%b)
# print(gcd(16,80))

#decimal to binary

# def D2b(num):
#     quo=int(num/2)
#     if num==0:
#         return quo
#     rem=num%2
#     return f'{D2b(quo)}{rem}'

# def D2b(n):
#     assert int(n)==n, 'The input number shld be an integer only'
#     if n==0:
#         return 0
#     else:
#         a=int(n/2)
#         b=n%2+10*D2b(int(n/2))
#         return b
# print(D2b(13))

# def power(base,exp):
#     if exp==0:
#         return 1
#     else:
#         return(base*power(base,exp-1))
# print(power(2,0) )# 1
# print(power(2,2) )# 4
# print(power(4,4) )# 16

def productOfArray(arr):
    if :
    lt=len(arr)
    return arr[]

productOfArray([1,2,3]) #6
productOfArray([1,2,3,10]) #60

