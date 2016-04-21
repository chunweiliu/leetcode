class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Figure out which row and column we are looking at.
        # A (1) every 10 number,
        # 10 1s every 100 number,
        # 100 1s every 1000 number.
        # -------------------------
        #  0   (1)   2   3  ...  9
        # 10  1(1)  12  13  ... 19
        # 20  2(1)  22  23  ... 29
        count = 0
        digit = 1
        while digit <= n:
            row, column = n / digit, n % digit
            count += ((row + 8) / 10 * digit +
                      (column + 1 if row % 10 == 1 else 0))
            digit *= 10
        return count

        # # Enumeration: O(nd)
        # count = 0
        # for i in range(1, n + 1):
        #     while i:
        #         count += i % 10
        #         i /= 10
        # return count
