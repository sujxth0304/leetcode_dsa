class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        sum = 0
        for i in range(len(nums)):
            mn = mx = nums[i]
            for j in range(i, len(nums)):
                mn = min(mn, nums[j])
                mx = max(mx, nums[j])
                sum += mx-mn
        return sum
