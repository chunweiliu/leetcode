class Solution(object):
    def __init__(self):
        # Use an instance variable to store existed rows.
        self.rows = []
        self.rows.append([1])
        self.rows.append([1, 1])

    def generate(self, num_rows):
        """
        :type numRows: int
        :rtype: List[List[int]]

        Example:
               1
             1   1
           1   2   1
         1   3   3   1
        """
        while len(self.rows) < num_rows:
            last_row = self.rows[-1]
            new_row = [1] + \
                      [last_row[i] + last_row[i + 1] for i in range(len(last_row) - 1)] + \
                      [1]
            self.rows.append(new_row)

        return self.rows[:num_rows]

if __name__ == "__main__":
    print Solution().generate(10)