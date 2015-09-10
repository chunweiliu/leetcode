class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        # Take care of sign.
        sign = -1 if dividend * divisor < 0 else 1
        dividend *= -1 if dividend < 0 else 1
        divisor *= -1 if divisor < 0 else 1

        # Accumulate the divsor faster by doubling it.
        quotient = 0
        factor_quotient, factor_divisor = 1, divisor

        while factor_divisor <= dividend:
            dividend -= factor_divisor
            quotient += factor_quotient
            factor_divisor += factor_divisor
            factor_quotient += factor_quotient
            # Reset the factor quotient for the next run
            if dividend < factor_divisor:
                factor_quotient, factor_divisor = 1, divisor

        # Handle the boundary cases
        ans = sign * quotient
        if ans > 2 ** 31 - 1:
            return 2 ** 31 - 1
        if ans < - 2 ** 31:
            return - 2 ** 31
        return sign * quotient

if __name__ == '__main__':
    dividend = -10
    divisor = -1
    print Solution().divide(dividend, divisor)
