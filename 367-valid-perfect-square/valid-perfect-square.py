class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l, r = 1, num
        while l <= r:
            mid = (l+r)//2
            mid_sq = mid*mid
            if mid_sq == num:
                return True
            elif num > mid_sq:
                l = mid + 1
            else:
                r = mid - 1
        return False