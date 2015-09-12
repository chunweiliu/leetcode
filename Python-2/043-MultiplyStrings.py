class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        # 1 2 3
        #   1 9
        product = [0] * (len(num1) + len(num2))
        for i, n in enumerate(reversed(num1)):
            for j, m in enumerate(reversed(num2)):
                product[i + j] += int(n) * int(m)
                product[i + j + 1] += product[i + j] // 10
                product[i + j] %= 10

        # Clear the initial zero elements in the back.
        while len(product) > 1 and product[-1] == 0:
            product.pop()
        return ''.join(map(str, reversed(product)))

        # Slow solution.
        # ans = 0
        # for i, n in enumerate(list(reversed(num2))):
        #     level, carry = 0, 0
        #     for j, m in enumerate(list(reversed(num1))):
        #         x = int(n) * int(m) + carry
        #         level += (x % 10) * 10 ** j
        #         carry = x // 10
        #     if carry:
        #         level += carry * 10 ** len(num1)
        #     level *= 10 ** i
        #     ans += level
        # return str(ans)

if __name__ == '__main__':
    num1 = '98'
    num2 = '9'
    print Solution().multiply(num1, num2)
