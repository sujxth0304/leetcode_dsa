class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        hashm = {}
        for num in nums:
            if num in hashm:
                return True
            else:
                hashm[num] = 1 + hashm.get(num, 0)
        return False
