class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def accumlated_product(nums):
            ans, prod = [], 1
            for num in nums:
                prod *= num
                ans.append(prod)
            return ans

        # Add shift since the rule of the product is
        # ans[i] = lefts[i-1] * rights[i+1]
        lefts = [1, 1] + accumlated_product(nums)
        rights = accumlated_product(nums[::-1])[::-1] + [1, 1]

        ans = []
        for (left, right) in zip(lefts, rights):
            ans.append(left * right)
        return ans[1:-1]  # Get rid of the shifted dummies.
