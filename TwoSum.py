class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        """Reduce range by two pointers
        Time: O(n log n)
        Space: O(1)
        Corner: return original index
        """
        if not num or len(num) < 2:
            return None

        sorted_num = sorted(enumerate(num), key=lambda num: num[1])

        p, q = 0, len(num) - 1
        while p < q:
            s = sorted_num[p][1] + sorted_num[q][1]
            if s == target:
                break
            if s > target:
                q -= 1
            else:
                p += 1

        # compute original index
        small, large = sorted_num[p][0]+1, sorted_num[q][0]+1
        if small > large:
            small, large = large, small
        return (small, large)
