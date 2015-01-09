"""
n = 1 1(2)
n = 2 -> n = 1 add (1)() ((2)) -> 1(2)3(4) (())
n = 3 -> n = 2 add (1)()() ((2))() no 3 but add 4 -> only add in () + aside
"""
def generateParenthesis(self, n):
    if n == 0:
        return []
    if n == 1:
        return ['()']

    ans = list()
    parenthesis = self.generateParenthesis(n - 1)
    for each in parenthesis:
        each_list = list(each)  # inside in each
        for i, one_side in enumerate(each_list):
            if i > 0 and i < len(each_list) and \
               one_side == '(' and each_list[i+1] == ')':
                copy = list(each_list)
                copy.insert(i+1, '()')
                ans.append(''.join(copy))
    ans.append('()'*n)
    return ans
