class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # profits = max profits of prices[:i] +
        #           max profist of prices[i:]
        n = len(prices)
        if n < 2:
            return 0

        left_profits = [0] * n
        lowest_price = prices[0]
        for i, price in enumerate(prices[1:], 1):
            left_profits[i] = max(left_profits[i - 1], price - lowest_price)
            lowest_price = min(lowest_price, price)

        # From the end. Be aware of the index.
        right_profits = [0] * n
        highest_price = prices[-1]
        for i, price in enumerate(list(reversed(prices[:-1])), 2):
            right_profits[-i] = max(0, highest_price - price)  # No propergate.
            highest_price = max(highest_price, price)

        # Zip: [(left_profits[0], right_profits[0]), ..., ]
        return max(map(sum, zip(left_profits, right_profits)))
