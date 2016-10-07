class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        effective_bits = bin(n)[2:]
        padded_bits = '0' * (32 - len(effective_bits)) + effective_bits
        reverse_bits = padded_bits[::-1]
        return int(reverse_bits, 2)
