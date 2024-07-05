# # BEST BUY OF A STOCK
# def maxProfit(prices):
#     buy_price=prices[0]
#     buy_day=1
#     sell_price=0
#     sell_day=0
#     for i in range(len(prices)-1):        
#         if buy_price>prices[i]:
#             buy_price=prices[i]
#             buy_day=i+1
#             print(f'Buy: day-{buy_day},price:{buy_price}')
#             # if i==len(prices)-1:
#             #     buy_price=0
#     for i in range(buy_day-1,len(prices)):
#         if prices[i]>buy_price and sell_price<prices[i]:
#             print(f'sell: day-{sell_day},price:{sell_price}')
#             sell_price=prices[i]
#             sell_day=i+1
#     print(buy_day,buy_price)
#     print(sell_day,sell_price)
#     print('Final Output:')
#     print(f'Buy day:{buy_day}, sell_day:{sell_day}')
#     print(f'Buy price:{buy_price}, sell price:{sell_price}, profit: {sell_price-buy_price}')
    
# def maxProfit(prices):
#     buy_price=prices[0]
#     profit=0
#     for i in range(1,len(prices)):
#         if buy_price>prices[i]:
#             buy_price=prices[i]
#         if (prices[i]-buy_price)>profit:
#             profit=-buy_price+prices[i]
#     return profit
# # prices = [7,1,5,3,6,4] #op=5
# # maxProfit(prices)
# # prices = [2,4,1] #op=0
# prices=[3,2,6,5,0,3]
# print(maxProfit(prices))


#Two sum and a target
#Approach-1
a=[1,4,7,11,9,6,2]
targ=13
# for i in range(0,len(a)):
#     for j in range(i,len(a)):
#         if a[i]+a[j]==targ:
#             print(i,j)

# one=a[0]
# for i in range(1,len(a)):
#     two=targ-one
#     if two in a[i:]:
#         print(i,one,two,targ)
#     one=a[i]


#122. Best Time to Buy and Sell Stock II


# def bestBuy(prices):
#     buy_price=prices[0]
#     profit=0
#     start=1
#     max_profit=0
#     for i in range(start,len(prices)):
#         start=i+1
#         print(i,buy_price,prices[i],max_profit)
#         if buy_price>prices[i]:
#             print(i,buy_price,prices[i],max_profit)
#             buy_price=prices[i]
#             print(i,buy_price,prices[i],max_profit)
#         else:
#             profit=prices[i]-buy_price
#             print(profit) 
#             buy_price=prices[i]
#             # start=i+1
#             max_profit=profit+max_profit 
#     return max_profit

# def bestBuy(prices):
#     buy_price=prices[0]
#     profit=0
#     for i in range(1,len(prices)):
#         if buy_price>prices[i]:
#             buy_price=prices[i]
#         else:
#             profit=profit+(prices[i]-buy_price)
#             buy_price=prices[i]
#     return profit
# price=[7,1,5,3,6,4]
# print(bestBuy(price))
    
# Reverse a sttring using recursion

# def rev(str):
#     rev_word=''
#     for i in str:
#         rev_word=i+rev_word
#     return rev_word
# print(rev('Hello'))

# def rev(str):
#     rev_word=''
#     str.remove
#     rev_word=rev(str[len(str)-1])+rev_word
#     return rev_word
# print(rev('Hello'))

