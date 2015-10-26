class Solution(object):
    def singleNumber(self, nums, k=3):
        """
        :type nums: List[int]
        :rtype: int
        """
        # An integer general is 32 bits.
        INT_BITS = 32
        bit_counter = [0] * INT_BITS

        # Accumulate bit counter. Reset the bit if it has accumulated k times.
        for num in nums:
            for i in range(INT_BITS):
                bit_counter[i] += (num >> i) & 1
                bit_counter[i] %= k

        # Calculate the int representation.
        single_number = (0 if bit_counter[INT_BITS-1] == 0 else
                         -2 ** (INT_BITS-1))
        for i in range(INT_BITS - 1):
            single_number += bit_counter[i] << i
        return single_number
