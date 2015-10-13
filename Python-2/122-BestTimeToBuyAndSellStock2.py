class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        #          d   Algo 1 earns: d - a
        #     b   /    Algo 2 earns: b - a + d - c
        #    /\  /
        #   /  \/
        #  /   c
        # a
        # The profits are aggregate, do transcation if there is no fee.
        profit = 0
        for i, price in enumerate(prices[1:], 1):
            profit += max(0, price - prices[i - 1])
        return profit
