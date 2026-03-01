class Solution:
    def minPartitions(self, n: str) -> int:
        best = 0
        for c in n:
            best = max(int(c), best)
        return best