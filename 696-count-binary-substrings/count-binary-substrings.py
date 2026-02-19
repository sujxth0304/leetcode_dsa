class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        prev = 0
        streak = 1
        sum = 0

        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                streak += 1
            else:
                sum += min(streak, prev)
                prev = streak
                streak = 1
        sum += min(streak, prev)
        return sum
