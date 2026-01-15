class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        maxSum = 0
        for num in nums:
            if maxSum < 0:
                maxSum = 0
            maxSum += num
            maxSub = max(maxSub, maxSum)
        return maxSub