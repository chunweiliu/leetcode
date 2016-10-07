class Solution(object):
    def majorityElement(self, numbers):
        """
        :type numbers: List[int]
        :rtype: List[int]

        Find all elements that appear more than n/3 times.

        Requirements:
        Time: O(n)
        Space: O(1)

        Observation:
        At most two elements can be found.
        """
        counts = [0, 0]
        things = [0, 0]
        for number in numbers:
            if number in things:
                counts[things.index(number)] += 1
            elif 0 in counts:
                things[counts.index(0)] = number
                counts[counts.index(0)] = 1
            else:
                counts[:] = [count - 1 for count in counts]
        return [thing for thing in set(things)
                if numbers.count(thing) > len(numbers) // 3]
        