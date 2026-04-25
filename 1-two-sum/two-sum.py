class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in hashMap:
                return [i, hashMap[diff]]
            else:
                hashMap[num] = i
                