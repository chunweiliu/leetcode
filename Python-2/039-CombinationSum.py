class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # Reduce the target to smaller ammount if possible.

    def combination_sum(self, candidates, target, ans):
        if target == 0:
            return True
        for number in candidates:
            if self.combination_sum(target - number):
                ans.append([])
