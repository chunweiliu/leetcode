class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        # Using k numbers from [1, ..., 9] to compose a sum n.
        results = []
        self.combination_sum(k, n, range(1, 10), [], results)
        return results

    def combination_sum(self, k, n, candidates, attemp, results):
        if k < 0 or n < 0:
            return
        if k == 0 and n == 0:
            results += [attemp]
        for i, c in enumerate(candidates):
            self.combination_sum(k - 1, n - c, candidates[i+1:],
                                 attemp + [c], results)

if __name__ == '__main__':
    k = 3
    n = 2
    print Solution().combinationSum3(k, n)
