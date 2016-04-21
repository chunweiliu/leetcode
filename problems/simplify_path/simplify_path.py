class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        # .. means go back to the previous folder
        # This problem is not easy to understand.
        stack = list()
        for item in path.split('/'):
            if item not in ['.', '..', '']:  # Good representation.
                stack.append(item)
            if item == '..' and stack:
                stack.pop()
        return '/' + '/'.join(stack)

if __name__ == '__main__':
    path = '/abc/...'
    print Solution().simplifyPath(path)
