class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        R = len(grid)
        C = len(grid[0])

        """
        50 * 50 ->
        each cell is the "center" -> how many length is there?
        50

        the number of rhombus -> 50 * 50 * 50
        * 50 for a loop
        """

        vals = SortedSet()

        def get_sum(x, y, L):
            if L == 0:
                return grid[x][y]

            # go to the top
            cx, cy = x - L, y
            total = 0

            # go bottom right
            for dx, dy in [[+1, +1], [+1, -1], [-1, -1], [-1, +1]]:
                for cL in range(L):
                    cx += dx
                    cy += dy

                    total += grid[cx][cy]
            return total

        for x in range(R):
            for y in range(C):
                # center at x, y
                L = 0
                while x - L >= 0 and x + L < R and y - L >= 0 and y + L < C:
                    t = get_sum(x, y, L)
                    vals.add(t)
                    if len(vals) > 3:
                        vals.remove(vals[0])
                    L += 1

        return list(reversed(vals))