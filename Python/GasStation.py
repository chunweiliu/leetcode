class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        """Record the gas need to be filled,
        check in the end if the need is satisfied
        Time: O(n)
        Space: O(1)
        """
        gas_left, gas_needed = 0, 0
        start = 0
        for i, (g, c) in enumerate(zip(gas, cost)):
            gas_left += g - c
            if gas_left < 0:
                gas_needed -= gas_left
                gas_left = 0
                start = i + 1
        return start if gas_left >= gas_needed else -1
