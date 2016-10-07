class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return ['']
        if n == 1:
            return ['()']
        combinations = self.generateParenthesis(n - 1)
        candidates = list()
        for x in combinations:
            for i in range(len(x)):
                candidates.append(x[:i] + '()' + x[i:])
        return list(set(candidates))

if __name__ == "__main__":
    n = 3
    print Solution().generateParenthesis(n)
