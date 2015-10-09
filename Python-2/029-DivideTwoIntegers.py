class Solution(object):
    def divide(self, n, m):
        """
        :type dividend (n): int
        :type divisor (m): int
        :rtype: int
        """
        # Take care of sign.
        # Negative value
        sign = 1
        if n * m < 0:
            sign = -1
        n = abs(n)  # [BUG] cannot handle n = -1, m = -1
        m = abs(m)

        # Zero divident
        if m == 0:
            return None

        q = 0
        factor_m = m
        factor_c = 1
        while n >= m:
            while n >= factor_m:
                n -= factor_m
                q += factor_c

                factor_m += factor_m
                factor_c += factor_c
            factor_m = m
            factor_c = 1

        ans = sign * q
        int_max = 2 ** 31 - 1
        int_min = - 2 ** 31
        if ans > int_max:
            ans = int_max
        if ans < int_min:
            ans = int_min
        return ans
