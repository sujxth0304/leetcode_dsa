class Solution:
    def climbStairs(self, n: int) -> int:
        # top down memoization
        # memo = {1:1, 2:2}
        # def f(n):
        #     if n in memo:
        #         return memo[n]
        #     else:
        #         memo[n] = f(n-1) + f(n-2)
        #         return memo[n]
        # return f(n)

        # bottom up tabulation
        if n == 1:
            return 1
        if n == 2:
            return 2
        dp = [0]*n
        dp[0] = 1
        dp[1] = 2
        for i in range(2, n):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n-1]