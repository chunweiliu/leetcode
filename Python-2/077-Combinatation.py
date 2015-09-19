class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        # Built-in python combination.
        # from itertools import combinations
        # return map(list, combinations(range(1, n + 1), k))

        # Recursive combination C(n, k) = C(n - 1, k - 1) + C(n - 1, k)
        #                                 ^choose #n        ^not choose #n

        # Pick the last element first, and choose the rest elements in front of
        # the last element, so in each selection the elements are in order.
        # E.g. 4C2: Pick 1 (no other available);
        #           Pick 2 [prev, 2], prev = [1]
        #           Pick 3 [prev, 3], prev = [1, 2]
        #           Pick 4 [prev, 4], prev = [1, 2, 3]

        # This is the key of recursion.
        # For those recursion calls didn't make it to k == 0, they retrun an
        # [], instead of a [[]]. A [] is not an iterable object, so the result
        # won't be change inside the for loop.
        if k == 0:
            return [[]]

        # return [prev + [i] for i in range(1, n + 1)
        #         for prev in self.combine(i - 1, k - 1)]

        # An visualization of the call stack.
        result = []
        for i in range(1, n + 1):
            # Pick i and compute the possible combination before i.
            # print 'i = %d, call combine(%d, %d)' % (i, i - 1, k - 1)

            for prev in self.combine(i - 1, k - 1):
                # The combine function has to reach to k == 0 to return an
                # "indentity element", which is [[]], for entering this block.
                # So k determines how deep the combine function can go through,
                # and also how many elements can be appended to the list.
                result.append(prev + [i])

                # print 'in combine(%d, %d)' % (i - 1, k - 1)
                # print 'result: ', result
        return result


if __name__ == '__main__':
    n, k = 4, 1
    print Solution().combine(n, k)
