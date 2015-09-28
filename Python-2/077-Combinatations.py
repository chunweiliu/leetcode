class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        # Recursive combination C(n, k) = C(n - 1, k - 1) + C(n - 1, k)
        #                                 ^choose #n        ^not choose #n

        # For those recursion calls didn't make it to k == 0, they retrun an
        # [], instead of a [[]]. A [] is not an iterable object, so the result
        # won't be change inside the for loop.
        if k == 0:
            return [[]]

        result = []
        for i in range(1, n + 1):
            # Pick i and compute the possible combination before i.
            for prev in self.combine(i - 1, k - 1):
                # The combine function has to reach to k == 0 to return an
                # "indentity element", which is [[]], for entering this block.
                # So k determines how deep the combine function can go through,
                # and also how many elements can be appended to the list.
                result.append(prev + [i])
        return result

        # # Or using list comprehasion.
        # if k == 0:
        #     return [[]]
        # return [prev + [i] for i in range(1, n + 1)
        #         for prev in self.combine(i - 1, k - 1)]

        # # Built-in python combination.
        # from itertools import combinations
        # return map(list, combinations(range(1, n + 1), k))

if __name__ == '__main__':
    n, k = 4, 2
    print Solution().combine(n, k)
