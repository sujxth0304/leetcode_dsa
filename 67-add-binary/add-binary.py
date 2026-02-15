class Solution:
    def addBinary(self, a: str, b: str) -> str:
        bin_a, bin_b = int(a, 2), int(b, 2)
        bin_sum = bin(bin_a + bin_b)

        return str(bin_sum[2:])
