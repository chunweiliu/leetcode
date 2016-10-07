class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        stack_min, stack_val = self.stack[-1] if self.stack else (10**10, None)
        stack_min = min(stack_min, x)
        self.stack.append((stack_min, x))

    def pop(self):
        """
        :rtype: nothing
        """
        if self.stack:
            self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1][1] if self.stack else None

    def getMin(self):
        """
        :rtype: int
        """
        return self.stack[-1][0] if self.stack else None


if __name__ == '__main__':
    stack = MinStack()
    stack.push(-3)
    print stack.top()
    stack.push(10)
    print stack.top()
    print stack.getMin()
