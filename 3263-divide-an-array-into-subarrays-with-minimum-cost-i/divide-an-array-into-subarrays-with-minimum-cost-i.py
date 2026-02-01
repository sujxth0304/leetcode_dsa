class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        cost = nums[0]
        rem_sorted = sorted(nums[1:])
        return (cost + rem_sorted[0] + rem_sorted[1])