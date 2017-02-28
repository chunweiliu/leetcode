"""Return all subsets of a list

    << [1, 2]
    => [[], [1], [2], [1, 2]]

    1) Append the new element to all current subsets

       []  [1]  [1, 2]
       ----------------
       []  []     []
           [1]    [1]
                  [2]
                  [1, 2]

    2) Binary tree

               []
              /  \
            #    [1]        add or not to add first 
           /\    / \
          # [2] #   [1, 2]  add of not to add second

"""

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 1)
        subsets = [[]]
        for n in sorted(nums):
            # [] is a element. It's like 0 in addition or 1 in multiplication.
            subsets += [s + [n] for s in subsets]
        return subsets

    def subsets2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 2)
        def helper(nums, i, attemp):
            if i == len(nums):
                subsets.append(attemp)
                return

            helper(nums, i + 1, attemp[:])
            helper(nums, i + 1, attemp + nums[i])

if __name__ == '__main__':
    nums = [1, 2, 3]
    print Solution().subsets(nums)
