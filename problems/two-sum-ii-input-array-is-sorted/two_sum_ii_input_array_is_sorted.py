class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]

        Given an array of integers that is already sorted in ascending order, 
        find two numbers such that they add up to a specific target number.

        * not zero-based
        * one and only one solution

        O(n): two pointers
        """
        head = 0
        tail = len(numbers) - 1
        while numbers[head] + numbers[tail] != target:
            if numbers[head] + numbers[tail] > target:
                tail -= 1
            else:
                head += 1
        return [head + 1, tail + 1]
