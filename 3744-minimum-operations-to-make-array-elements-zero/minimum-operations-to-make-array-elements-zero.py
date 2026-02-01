class Solution:
    def get(self, n):
        if n <= 0:
            return 0

        res = 0
        power = 1   # 4^k
        ops = 1     # operations needed in this range

        while power <= n:
            next_power = power * 4
            count = min(n, next_power - 1) - power + 1
            res += count * ops

            power = next_power
            ops += 1

        return res

    def minOperations(self, queries: List[List[int]]) -> int:
        ans = 0
        for l, r in queries:
            total = self.get(r) - self.get(l - 1)
            ans += (total + 1) // 2
        return ans
