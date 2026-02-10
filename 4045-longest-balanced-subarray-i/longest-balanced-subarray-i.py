class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        max_length = 0

        for i in range(n):
            even, odd = set(), set()
            for j in range(i, n):
                if nums[j]%2 == 0:
                    even.add(nums[j])
                else:
                    odd.add(nums[j])
                if len(even) == len(odd):
                    max_length = max(max_length, j-i + 1)
        return max_length
