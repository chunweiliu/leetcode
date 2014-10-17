class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        """Fix a and search b + c = -a
        Time: O(n^2)
        Space: O(1)
        Corner: duplicates in b, c
        """
        if not num and len(num) < 2:
            return []

        ans = list()
        num.sort()
        for i, a in enumerate(num):
            # avoid duplicates in a
            if i > 0 and a == num[i - 1]:
                continue

            j, k = i+1, len(num)-1
            while j < k:
                # avoid duplicates in b, c
                while j > i+1 and num[j] == num[j - 1] and j < k:
                    j += 1

                while k < len(num)-1 and num[k] == num[k + 1] and j < k:
                    k -= 1

                b, c = num[j], num[k]
                if a + b + c == 0:
                    ans.append([a, b, c])
                    j += 1
                    k -= 1
                elif a + b + c < 0:
                    j += 1
                else:
                    k -= 1
        return ans


if __name__ == "__main__":
    num = [-1, 0, 1, 2, -1, -4]
    print Solution().threeSum(num)
