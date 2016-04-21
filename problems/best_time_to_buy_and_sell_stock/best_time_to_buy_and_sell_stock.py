class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        # If the number of transcations is larger than the maximum
        # buy-sell times. Just accumulate all the profits.
        if k >= len(prices) / 2:
            profit = 0
            for i, price in enumerate(prices[1:], 1):
                balance = price - prices[i - 1]
                if balance > 0:
                    profit += balance
            return profit

        # Otherwise, DP.
        balance = [-max(prices)] * (k + 1)
        profits = [0] * (k + 1)
        for price in prices:
            for j in range(1, k + 1):
                # Whether to buy.
                # Because balance[j] gain from the profits[j - 1], the
                # more k, the more profits.
                balance[j] = max(balance[j], profits[j - 1] - price)

                # Whether to sell.
                profits[j] = max(profits[j], balance[j] + price)
        return profits[k]
