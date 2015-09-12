class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # return x ** n

        # Might cause stack overflow
        # if n == 1:
        #     return x
        # return n * self.myPow(x, n - 1)

        if n < 0:
            return 1 / self.pow(x, -n)
        return self.pow(x, n)

    # def divided_pow(self, x, n):
    #     # Assume n is non-negative
    #     # This is still slow, because it creates duplicate trees.
    #     if n == 0:
    #         return 1
    #     if n == 1:
    #         return x
    #     if n % 2 == 0:
    #         return self.divided_pow(x, n // 2) * self.divided_pow(x, n // 2)
    #     return x * self.divided_pow(x, n // 2) * self.divided_pow(x, n // 2)

    def pow(self, x, n):
        # 8 = 1 0 0 0
        d = x
        ans = 1
        while n:
            if n & 1:
                ans *= d
            d = d * d
            n >>= 1
        return ans

if __name__ == '__main__':
    x = 2.0
    n = 4
    print Solution().myPow(x, n)
