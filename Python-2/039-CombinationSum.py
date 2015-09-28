class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # Reduce the target to smaller ammount if possible.
        ans = list()
        self.combination_sum(sorted(candidates), target, [], ans)
        return ans

    def combination_sum(self, candidates, target, attemp, ans):
        if target == 0:
            ans += [attemp]
            return
        for i, number in enumerate(candidates):
            if number <= target:
                self.combination_sum(
                    candidates[i:], target - number, attemp + [number], ans)

if __name__ == '__main__':
    candidates = [2, 3, 6, 7]
    target = 7
    print Solution().combinationSum(candidates, target)
