class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        return self.combination_sum(sorted(candidates), target)

    def combination_sum(self, candidates, target, attemp=[], ans=[]):
        if target == 0:
            ans += [attemp]
            return ans
        for i, number in enumerate(candidates):
            if number <= target:
                self.combination_sum(
                    candidates[i:], target - number, attemp + [number], ans)
        return ans

    def combination_sum_stack(self, candidates):
        ans = []
        stack = [(0, 0, [])]
        while stack:
            index, current_sum, attemp = stack.pop()
            if current_sum == target:
                ans.append(attemp)
            for n in candidates[index:]:
                if current_sum <= target:
                    stack.append(index + n, current_sum + n, attemp + [n])
        return ans


if __name__ == '__main__':
    candidates = [2, 3, 6, 7]
    target = 7
    print Solution().combinationSum(candidates, target)
