class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Corner case 0:
        if n == 0:
            return 0

        f = [0] * (n + 1)
        f[0] = 1  # Set up indentity element for the joint condition.

        for i in range(1, n + 1):
            # f_i has the following conditions:
            # 1 as root, not left and n - 1 nodes on the right,
            # 2 as root, 1 left and n - 2 nodes on the right, ...
            # i as root, n - 1 left and 0 right.
            n_bst = 0
            for j in range(i):
                n_bst += f[j] * f[i - j - 1]
            f[i] = n_bst
        return f[n]
