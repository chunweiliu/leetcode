class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        # The ugly numbers are generated from the one of three series.
        # 1 * 2, 2 * 2, 3 * 2, 4 * 2, 5 * 2, 6 * 2, 8 * 2, ...
        # 1 * 3, 2 * 3, 3 * 3, 4 * 3, 5 * 3, 6 * 3, 8 * 3, ...
        # 1 * 5, 2 * 5, 3 * 5, 4 * 5, 5 * 5, 6 * 5, 8 * 5, ...

        # Merge Sort
        u = [1]
        p2, p3, p5 = 0, 0, 0
        for _ in range(1, n):
            u2, u3, u5 = u[p2] * 2, u[p3] * 3, u[p5] * 5
            u.append(min([u2, u3, u5]))

            # Both 6 * 2 and 4 * 3 need to be moved.
            p2 += u[-1] == u2
            p3 += u[-1] == u3
            p5 += u[-1] == u5
        return u[-1]
