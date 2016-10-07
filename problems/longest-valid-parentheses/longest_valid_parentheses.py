class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Meet a ')', count the length if the stack top is a '('.
        # Count the length only use the top element on the stack. It means
        # between the top element to the current element (i), all parentheses
        # have been paired together.
        longest_length = 0
        stack = list()
        for i, c in enumerate(s):
            if c == ')':
                if len(stack) > 0 and s[stack[-1]] == '(':
                    stack.pop()  # The top one has pair, get rid of the index.
                    if len(stack) == 0:  # All clearance
                        longest_length = i + 1
                    else:
                        longest_length = max(longest_length, i - stack[-1])
                else:
                    # Put a ')' into the stack if it didn't match '('. So next
                    # time his ')' could be a starter of the new substring.
                    stack.append(i)
            else:
                stack.append(i)
        return longest_length

if __name__ == '__main__':
    s = '(()()'
    print Solution().longestValidParentheses(s)
