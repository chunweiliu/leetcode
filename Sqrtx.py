class Solution:
    # @param x, an integer
    # @return an integer
    def sqrt(self, x):
        if x < 2:
            return x
        sml = 0
        lrg = x
        while abs(lrg - sml) > 0.1:
            xsqrt = (sml + lrg) / 2.0
            print xsqrt, sml, lrg
            if xsqrt * xsqrt > x:
                lrg = xsqrt
            else:
                sml = xsqrt
        return int(xsqrt)

if __name__ == "__main__":
    # x = 509023048
    x = 9
    # x = 0
    # x = 1
    # x = 3
    print Solution().sqrt(x)
