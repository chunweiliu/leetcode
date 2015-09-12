class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # Recursively find the solution, eleminate candidates in recursion.
        ans = []
        candidates.sort()
        self.combination_sum(candidates, target, [], ans)
        return ans

    def combination_sum(self, candidates, target, attemp, ans):
        if target == 0:
            ans += [attemp]
            return
        for i, number in enumerate(candidates):
            if number <= target and (i == 0 or
                                     # Don't pick the same one in same level.
                                     candidates[i] != candidates[i - 1]):
                self.combination_sum(
                    candidates[i+1:], target - number, attemp + [number], ans)

if __name__ == '__main__':
    candidates = [1, 1, 2]
    target = 3
    print Solution().combinationSum2(candidates, target)
