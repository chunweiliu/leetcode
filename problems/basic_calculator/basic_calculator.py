class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        # '1 + 2' -> 3
        total = 0
        sign = 1
        num = 0
        stack = []
        for c in s:
            if c.isdigit():
                num = 10 * num + int(c)  # Get the correct number from strings
                continue
            total += sign * num
            num = 0

            if c == '+':
                sign = 1
            elif c == '-':
                sign = -1
            elif c == '(':
                stack.append(total)
                stack.append(sign)
                total = 0  # Like the Cn in calculator
                sign = 1
            elif c == ')':
                total *= stack.pop()  # sign
                total += stack.pop()  # total

        return sign * num + total

if __name__ == '__main__':
    s = '10'
    print Solution().calculate(s)
