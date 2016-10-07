class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int

        Problem: Count the number of prime numbers LESS THAN a non-negative number, n.

        Sieve of Eratosthenes
        Time: O(n log log n)

        for number less than n^(1/2): -> O(n)
            do the sieve operation: -> O(log log n)

        Prove the sieve operation is lower than O(log n)
            H_p = 1 + 1/2 + 1/3 + ... + 1/p
            H_n = 1 + 1/2 + 1/3 + ... + 1/n
            H_e = 1 + 1/2 + 1/4 + 1/4 + 1/8 + 1/8 + 1/8 + 1/8 + ... 1/log_2(n)
                = 1 + 1/2 +    1/2    +          1/2          + ...
                = 1 + 1/2 * log_2(n)

            O(H_p) <= O(H_e) <= O(H_n)  (1)

            O(H_e) = O(log n)

            With (1), O(H_p) <= O(log n)
        """
        from math import ceil

        sieves = [1] * n
        if sieves:
            sieves[0] = 0
        if n > 1:
            sieves[1] = 0

        for number in range(2, int(ceil(n ** 0.5))):
            if sieves[number] == 0:
                continue

            multiple = number + number 
            while multiple < n:
                sieves[multiple] = 0
                multiple += number

        return sum(sieves)

if __name__ == "__main__":
    print '-'
    print Solution().countPrimes(0)  # 0 
    print Solution().countPrimes(1)  # 0
    print Solution().countPrimes(2)  # 0  
    print Solution().countPrimes(3)  # 1
    print Solution().countPrimes(4)  # 2
    print Solution().countPrimes(9)  # 4
