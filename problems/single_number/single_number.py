class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def xor(x, y):
            return x ^ y
        a_xor_b = reduce(xor, nums)

        # Find the first different bit for seperating the two number a and b.
        the_first_different_bit = 0
        while a_xor_b & 1 == 0:
            print a_xor_b
            a_xor_b >>= 1
            the_first_different_bit += 1

        group_a, group_b = [], []
        for num in nums:
            if (num >> the_first_different_bit) & 1:
                group_a.append(num)
            else:
                group_b.append(num)

        return [reduce(xor, group_a), reduce(xor, group_b)]
