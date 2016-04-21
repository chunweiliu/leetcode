class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.push_stack = []
        self.pop_stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.push_stack.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        self.dump()
        self.pop_stack.pop()

    def peek(self):
        """
        :rtype: int
        """
        self.dump()
        return self.pop_stack[-1]

    def empty(self):
        """
        :rtype: bool
        """
        if not self.push_stack and not self.pop_stack:
            return True
        return False

    def dump(self):
        if len(self.pop_stack) == 0:
            while len(self.push_stack) != 0:
                self.pop_stack.append(self.push_stack.pop())
