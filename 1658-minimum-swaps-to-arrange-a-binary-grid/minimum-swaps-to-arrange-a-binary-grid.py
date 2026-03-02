class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)

        rows = []
        for i in range(n):
            farthest = -1
            for j in range(n):
                if grid[i][j] == 1:
                    farthest = j
            rows.append(farthest)
        count = 0
        for i in range(n):
            for j in range(len(rows)):
                if rows[j] <= i:
                    count += j
                    rows = rows[:j] + rows[j + 1:]
                    break
            else:
                return -1
        return count
