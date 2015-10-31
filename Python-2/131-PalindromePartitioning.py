class Solution(object):
    def partition(self, text):
        """
        :type text: str
        :rtype: List[List[str]]
        """
        ans = []
        for i in range(1, len(text) + 1):
            if text[:i] == text[i-1::-1]:
                for rest in self.partition(text[i:]):
                    ans.append([text[:i]] + rest)

        if not ans:
            return [[]]
        return ans
