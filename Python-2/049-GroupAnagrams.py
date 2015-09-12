from collections import defaultdict


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # Simple hash function has collection for the cases: 'duh' and 'ill'.
        # hist = defaultdict(list)
        # for s in strs:
        #     x = 0
        #     for c in s:
        #         x += hash(c)
        #     hist[x].append(s)
        #     hist[x].sort()
        # return [hist[key] for key in hist.keys()]

        # Tuple hash
        hist = defaultdict(list)
        for s in strs:
            x = tuple(sorted(s))
            hist[x].append(s)
        for value in hist.values():
            value.sort()
        return [hist[key] for key in hist.keys()]


if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print Solution().groupAnagrams(strs)
