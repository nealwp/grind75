"""
Problem:
    You are given an array prices where prices[i] is the price of a given stock on the ith day.
    You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
    Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
v1:
    -- set maxProfit to 0
    -- iterate through the list, calculate profit for each subsequent day
    -- if profit is greater than maxProfit, update maxProfit
    -- return maxProfit

    ** breaks on time limit exceed for giant list **
"""
import math
from time import perf_counter
from typing import List
from xmlrpc.client import MAXINT

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        for buy_day, buy_price in enumerate(prices):
            for sell_day, sell_price in enumerate(prices):
                if buy_day < sell_day:
                    profit = sell_price - buy_price
                    if profit > maxProfit:
                        maxProfit = profit
                continue

        return maxProfit
"""
v2:
    -- add conditional to stop loop if first element is highest price
    ** jk that's dumb, lol. doesn't work because sometimes there's a profit between
        the lowest day and the highest day
"""

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        if prices[0] == max(prices):
            return maxProfit
        for buy_day, buy_price in enumerate(prices):
            for sell_day, sell_price in enumerate(prices):
                if buy_day < sell_day:
                    profit = sell_price - buy_price
                    if profit > maxProfit:
                        maxProfit = profit
                continue

        return maxProfit

"""
v3:
    -- instead, shorten the list after each iteration
    -- and we don't care about the index of sell day anymore
    ** this still takes too long on big list **
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        for buy_day, buy_price in enumerate(prices):
            for sell_price in prices[buy_day:]:
                    profit = sell_price - buy_price
                    if profit > maxProfit:
                        maxProfit = profit
            continue

        return maxProfit
"""
v4:
    -- before we start iterating through the sell days, check if the max in the remaining list
        is bigger than buy price. if not, continue and no sell loop

    ** this one fails for time limit on large list, but this is th one in random order.
        earlier fails were for big list in descending order **
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        for buy_day, buy_price in enumerate(prices):
            if buy_price >= max(prices[buy_day:]):
                continue
            for sell_price in prices[buy_day:]:
                    profit = sell_price - buy_price
                    if profit > maxProfit:
                        maxProfit = profit
            continue

        return maxProfit

"""
v5:
    -- almost there. instead of looping through after checking if buy_price is max, just set the 
        profit to buy_price - max_price if the condition is false.
    -- if profit is larger than max_profit, update max_profit
    -- no more nested loop

    ** still fails for time limit on the large, random order list **
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for buy_day, buy_price in enumerate(prices):
            if buy_price >= max(prices[buy_day:]):
                continue
            else:
                profit = max(prices[buy_day:]) - buy_price
                if profit > max_profit:
                    max_profit = profit
            continue

        return max_profit

"""
v6:
    -- if the sell price is the biggest number left in the list,
        stop iterating!

    ** same fail as above ** 
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for buy_day, buy_price in enumerate(prices):
            if buy_price >= max(prices[buy_day:]):
                continue
            else:
                sell_price = max(prices[buy_day:])
                profit = sell_price - buy_price
                if profit > max_profit:
                    max_profit = profit
                    if sell_price > max(prices[buy_day+1:]):
                        break
            continue

        return max_profit
"""
v7:
    -- set the best selling price to nothing
    -- set the best buying price to the maximum possible value
        ^ notice that these are logically inverted, the opposite of the desired result
    -- iterate through the prices
        -- if the current price is less than best buying price, update the buying price
        -- otherwise, compare the current profit to the best sell
            -- if the current profit is better, update the best_sell
    -- return the best sell as the profit
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best_sell = 0
        best_buy = (10**5)
        for price in prices:    
            if price < best_buy:    
                best_buy = price  
            else:
                current_profit = price - best_buy
                if best_sell < current_profit:
                    best_sell = current_profit
        return best_sell

"""
Results:
Runtime: 1302 ms, faster than 68.61% of Python3 online submissions for Best Time to Buy and Sell Stock.
Memory Usage: 25 MB, less than 37.78% of Python3 online submissions for Best Time to Buy and Sell Stock.

"""