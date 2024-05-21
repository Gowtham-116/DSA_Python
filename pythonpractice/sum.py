# a,b,c=[eval(x) for x in input().split(',')]
# print(type(a),type(b),type(c))
# print(a,b,c)

# from sys import *
# sum1=0
# print(type(argv),argv)
# for x in argv[1:]:
#     sum1+=int(x)
# print(sum1)

# def fac(n):
#     if n==0:
#         fact=1
#     else:
#         fact=n*fac(n-1)
#     return fact
# print(fac(3))

import re

url = 'http://google.com/token:abcd?name:alex'

# Define a regular expression pattern to capture the token and name in any order
pattern = re.compile(r'(?:token:(\w+)\?name:(\w+))|(?:name:(\w+)\?token:(\w+))')

# Use the pattern to find matches in the URL
match = pattern.search(url)

# Check if there is a match
if match:
    # Extract token and name from the matched groups
    token = match.group(1) or match.group(4)
    name = match.group(2) or match.group(3)

    print("Token:", token)
    print("Name:", name)
else:
    print("No match found.")
