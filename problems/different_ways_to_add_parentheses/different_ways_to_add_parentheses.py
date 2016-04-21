class Solution(object):
    def __init__(self):
        self.operate = {'-': lambda x, y: x - y,
                        '+': lambda x, y: x + y,
                        '*': lambda x, y: x * y}

    def diffWaysToCompute(self, expression):
        """
        :type expression: str
        :rtype: List[int]
        """
        if expression.isdigit():
            return [int(expression)]

        ans = []
        for i, operator in enumerate(expression):
            # Divide and conquer
            if operator in '-+*':
                left_sums = self.diffWaysToCompute(expression[:i])
                right_sums = self.diffWaysToCompute(expression[i+1:])
                ans += [self.operate[operator](left, right)
                        for left in left_sums
                        for right in right_sums]
        return ans
