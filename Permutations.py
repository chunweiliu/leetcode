class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
        # Recursivly add a new member between old members
        # Time: O(n!)
        # Space: O(n)
        if len(num) == 1:
            return [num]
        else:
            new_num = num.pop()
            permuted_num = self.permute(num)

            ret = list()
            for x in permuted_num:
                for y in range(len(x) + 1):
                    new_list = list(x)
                    new_list.insert(y, new_num)
                    ret.append(new_list)
            return ret


if __name__ == "__main__":
    num = [1, 2, 3]
    print Solution().permute(num)
