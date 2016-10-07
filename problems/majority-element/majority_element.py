class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        The majority element is the element that appears more than lower(n/2) times.
        Assume that the majority element always exist in the array.

        * Count the array
        - Time: O(n)
        - Space: O(n). Use defaultdict.
          Space: O(1). Only two kinds: majority or others. The former is always greater.
        """
        # Assume the first on is thethe majority.
        majority = nums[0]
        count = 1
        for num in nums[1:]:
            # The number for the others are equal to the majority, switch their roles.
            if count == 0:
                majority = num
                count = 1
            elif majority == num:
                count += 1
            else:
                count -= 1
        return majority        

if __name__ == "__main__":
    nums = [1, 1, 0, 1, 0, 1]
    print Solution().majorityElement(nums)