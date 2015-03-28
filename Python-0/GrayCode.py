class Solution:
    # @return a list of integers
    def grayCode(self, n):
        if n == 0:
            return [0]

        # generate gray codes
        num = [[0] * n, [0] * (n - 1) + [1]]
        m = int(n)
        while n > 1:
            more_num = map(list, num)  # every list elements need to be copied
            more_num.reverse()
            for x in range(len(more_num)):
                more_num[x][n - 2] = 1
            n -= 1
            num += more_num

        # change the code into decimal
        decimal = list()
        for x in range(len(num)):
            a = 0
            for y in range(len(num[x])):
                a += num[x][y] * (1 << m - y - 1)
            decimal.append(a)
        return decimal

if __name__ == "__main__":
    print Solution().grayCode(0)
