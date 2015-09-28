class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort()
        h_index = 0
        for i, citation in enumerate(list(reversed(citations))):
            if citation >= i + 1:
                h_index = i + 1
            else:
                break
        return h_index

if __name__ == '__main__':
    citations = [3, 0, 6, 1, 5]
    print Solution().hIndex(citations)
