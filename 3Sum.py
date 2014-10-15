class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    MAXNUM = 100

    def threeSum(self, num):
        # Reduce to 2Sum
        # Time:O(n^2)
        # Space: O(MAXNUM)
        if len(num) == 0:
            return

        min_num = min(num)
        A = [n - min_num for n in num]
        A.sort()

        ans = list()
        prev_a = None
        for x in range(len(A)):
            a = A[x]
            if a == prev_a:
                continue

            b_and_cs = self.twoSum(A[x+1:], -3*min_num - a)  # why -3*min_num?
            for bc in b_and_cs:
                ans.append([a] + bc)
            prev_a = a

        # add min_num back
        for abc in ans:
            abc[0] += min_num
            abc[1] += min_num
            abc[2] += min_num
        return ans

    def twoSum(self, num, target):
        # find all pairs have sum equal to target
        # Time: O(n)
        # Space: O(MAXNUM)
        A = [0] * self.MAXNUM
        for n in num:
            A[n] += 1

        ans = list()
        for x in range(len(A)):
            if A[x] > 0:  # Once you count an entry, it has to be eliminated
                A[x] -= 1
                if A[target - x] > 0:
                    A[target - x] -= 1
                    ans.append([x, target - x])

        return ans

if __name__ == "__main__":
    num = [-1, 0, 1, 2, -1, -4]
    print Solution().threeSum(num)
