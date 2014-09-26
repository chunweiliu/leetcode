class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        # Brute force. Time O(n^2) -> TLE, you want to store the index
        # Don’t add up redundantly. Time O(n)
        in_tank, total = 0, 0
        start = -1
        for x in range(len(gas)):
            in_tank += gas[x] - cost[x]
            total += gas[x] - cost[x]
            if in_tank < 0:
                start = x
                in_tank = 0
        return start + 1 if total >= 0 else -1
