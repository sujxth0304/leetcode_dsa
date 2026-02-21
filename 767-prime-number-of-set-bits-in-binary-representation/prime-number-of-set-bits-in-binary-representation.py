class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        primes = set([2,3,5,7,11,13,17,19,23])

        def good(target):
            return bin(target).count("1") in primes

        count = 0
        for x in range(left, right+1):
            if good(x):
                count += 1
        return count