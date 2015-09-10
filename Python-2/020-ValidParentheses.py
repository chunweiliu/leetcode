class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # ({[]}), [](){}, [{}()]
        mapping = {'(': ')', '[': ']', '{': '}'}
        stack = list()
        for c in s:
            if c in mapping.keys():
                stack.append(c)
            else:
                if not stack or c != mapping[stack[-1]]:
                    return False
                stack.pop()
        return not stack

if __name__ == "__main__":
    s = '((){}){})'
    print Solution().isValid(s)
