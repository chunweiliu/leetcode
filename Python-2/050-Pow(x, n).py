from timeit import Timer
import timeit


class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            return 1 / self.pow1(x, -n)
        return self.pow1(x, n)

    def pow1(self, x, n):
        # 8 = 1 0 0 0
        d = x
        ans = 1
        while n:
            if n & 1:
                ans *= d
            d = d * d
            n >>= 1
        return ans

    def pow2(self, x, n):
        r = 1
        factor_x = x
        factor_c = 1
        while n:
            while n >= factor_c:  # [BUG] n > factor_c
                r *= factor_x
                n -= factor_c
                factor_x *= factor_x
                factor_c += factor_c
            factor_x = x
            factor_c = 1
        return r


if __name__ == '__main__':
    x = 2
    n = 10
    print (Solution().myPow(x, n) == Solution().pow1(x, n) ==
           Solution().pow2(x, n) == pow(x, n))

    print(timeit.timeit("pow(2, 10)"))

    t = Timer(lambda: Solution().myPow(2, 10))
    print t.timeit()

    t = Timer(lambda: Solution().pow1(2, 10))
    print t.timeit()

    t = Timer(lambda: Solution().pow2(2, 10))
    print t.timeit()
