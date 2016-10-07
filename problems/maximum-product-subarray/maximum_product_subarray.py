class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        Find the contiguous subarray within an array (containing at least one number)
        which has the largest product.

        Example: 

            2 * 3 * 0 * -2 * -2 
        min 2   3   0   -2   -2
        max 2   6   0    0    4
        """
        overall_max = max_product = min_product = nums[0]
        for num in nums[1:]:
            # Make the comparing statements easier.
            if num < 0:
                min_product, max_product = max_product, min_product

            # If the previous product is zero, than consider this number.
            max_product = max(num, max_product * num)
            min_product = min(num, min_product * num)

            overall_max = max(max_product, overall_max)

        return overall_max

nums = [2, 3, 0, -2, -2]
print Solution().maxProduct(nums)
        