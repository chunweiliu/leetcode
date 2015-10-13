class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        if not prices:
            return max_profit

        lowest_buy_price = prices[0]
        for sell in prices[1:]:
            max_profit = max(max_profit, sell - lowest_buy_price)
            lowest_buy_price = min(lowest_buy_price, sell)
        return max_profit
