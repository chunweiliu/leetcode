class Solution(object):
    def getRow(self, row_index):
        """
        :type row_index: int
        :rtype: List[int]

        Space: O(n)

        Example:
               1
             1   1
           1   2   1
         1   3   3   1 <-
        """
        start_index = 0
        if row_index == start_index:
            return [1]

        start_index += 1
        if row_index == start_index:
            return [1, 1]

        last_row = [1, 1]
        for _ in range(start_index, row_index):
            last_row = [1] + [last_row[i] + last_row[i + 1] for i in range(len(last_row) - 1)] + [1]
        return last_row
        
if __name__ == "__main__":
    print Solution().getRow(5)
