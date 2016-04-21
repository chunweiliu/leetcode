class Solution(object):
    def myAtoi(self, s):
        """
        :type str: s
        :rtype: int
        """
        def boundary_check(x):
            if x > 2 ** 31 - 1:
                return 2 ** 31 - 1
            if x < -2 ** 31:
                return -2 ** 31
            return x

        # Get rid of the invalid characters in the front
        n = 0
        sign = 1
        check = False
        for c in s:
            if not check:
                if c == " ":
                    continue
                if c == "+":
                    check = True
                    continue
                if c == "-":
                    sign = -1
                    check = True
                    continue

            check = True
            if not c.isdigit():
                return boundary_check(sign * n / 10)

            n += int(c)
            n *= 10

        return boundary_check(sign * n / 10)

if __name__ == "__main__":
    print Solution().myAtoi("2147483648")
