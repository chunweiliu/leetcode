class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        if len(version1) < len(version2):
            return -self.compareVersion(version2, version1)

        version1 = map(int, version1.split('.'))
        version2 = map(int, version2.split('.'))
        version2 += [0] * (len(version1) - len(version2))
        for v1, v2 in zip(version1, version2):
            if v1 > v2:
                return 1
            if v2 > v1:
                return -1
        return 0
