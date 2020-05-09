"""
=========================================================================================
122. Best Time to Buy and Sell Stock II
maxProfit()
<https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/>
<https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/564/>
=========================================================================================

Say you have an array prices for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. 
You may complete as many transactions as you like
(i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time
(i.e., you must sell the stock before you buy again).

Example 1:
----------
Input: [7, 1, 5, 3, 6, 4]
Output: 7
Explanation: Buy on day 2 (price=1) and sell on day 3 (price=5), profit = 5-1 = 4.
Then buy on day 4 (price=3) and sell on day 5 (price=6), profit = 6-3 = 3.


Example 2:
----------
Input: [1, 2, 3, 4, 5]
Output: 4
Explanation: Buy on day 1 (price=1) and sell on day 5 (price=5), profit = 5-1 = 4.
Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
engaging multiple transactions at the same time. You must sell before buying again.


Example 3:
----------
Input: [7, 6, 4, 3, 1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

Constraints:
------------
1 <= prices.length <= 3 * 10 ^ 4
0 <= prices[i] <= 10 ^ 4
"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        
        Runtime: 48 ms, faster than 73.65% of Python online submissions for Best Time to Buy and Sell Stock II.
        Memory Usage: 13.7 MB, less than 9.30% of Python online submissions for Best Time to Buy and Sell Stock II.
        """

        profit = 0
        for i in range(len(prices)-1):
            if len(prices) == 1:
                return 0
            elif prices[i] < prices[i+1]:
                profit += (prices[i+1] - prices[i])

        return profit

    def maxProfit_1(self, prices):
        """
        :type prices: List[int]
        :rtype: int

        Runtime: 52 ms, faster than 49.75% of Python online submissions for Best Time to Buy and Sell Stock II.
        Memory Usage: 13.7 MB, less than 9.30% of Python online submissions for Best Time to Buy and Sell Stock II.
       
        Runtime: 40 ms, faster than 97.84% of Python online submissions for Best Time to Buy and Sell Stock II.
        Memory Usage: 13.8 MB, less than 9.30% of Python online submissions for Best Time to Buy and Sell Stock II.
        """
        # buy low sell high
        # need min and max

        buy = -1 
        sell = -1
        profit = 0
        
        for i in range(len(prices)):
            if buy >= 0:
                if prices[i] > buy:
                    sell = prices[i]
                    profit += sell - buy
                    buy = -1

            if buy < 0:
                if prices[i:i+1] < prices[i+1:i+2]:
                    buy = prices[i]
                
        return profit

if __name__ == "__main__":
    # Input = Stock price per day
    # Output = Profit
    Input1 = [7, 1, 5, 3, 6, 4]   
    Output1 = 7
    Input2 = [1, 2, 3, 4, 5]
    Output2 = 4
    Input3 = [7, 6, 4, 3, 1]
    Output3 = 0
    input4 = [2,1,2,0,1]
    output4 = 2
    input5 = [5]
    output5 = 0

    s = Solution()
    a = s.maxProfit(Input1)
    b = s.maxProfit(Input2)
    c = s.maxProfit(Input3)
    d = s.maxProfit(input4)
    e = s.maxProfit(input5)

    print(a, b, c, d, e)
    pass
