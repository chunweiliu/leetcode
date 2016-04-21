class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if k == 0:
            return False

        # Use an ordered dictionary as buckets.
        # Each bucket contains elements with difference in t.
        # So check the i - 1, i, and i + 1 buckets, we will know if the
        # difference is within t.
        from collections import OrderedDict
        dic = OrderedDict()

        for num in nums:
            key = num // t if t else num
            for near_num in [dic.get(key - 1), dic.get(key), dic.get(key + 1)]:
                if near_num is not None and abs(near_num - num) <= t:
                    return True

            # There are k buckets and each bucket would have only one element.
            # If we have a bucket with two elements, our program should return
            # true above.
            if dic and len(dic) == k:
                dic.popitem(last=False)  # FIFO

            dic[key] = num

        return False
