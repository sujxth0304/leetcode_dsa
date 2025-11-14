class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashM = {}
        for i,n in enumerate(nums):
            if target-n in hashM:
                return [i, hashM[target-n]]
            hashM[n] = i