fmin = lambda x, y: x if x < y else y
fmax = lambda x, y: x if x > y else y
INF = 10 ** 9

class SegmentTree:
    def __init__(self, N):
        self.N = N
        self.minv = [0] * (4 * N)
        self.maxv = [0] * (4 * N)
        self.push = [0] * (4 * N)

    def _push(self, node):
        if self.push[node] != 0:
            self.minv[node * 2 + 1] += self.push[node]
            self.maxv[node * 2 + 1] += self.push[node]
            self.push[node * 2 + 1] += self.push[node]

            self.minv[node * 2 + 2] += self.push[node]
            self.maxv[node * 2 + 2] += self.push[node]
            self.push[node * 2 + 2] += self.push[node]

            self.push[node] = 0

    def _range_add(self, node, nodel, noder, left, right, incr):
        if right < nodel or noder < left:
            return

        if left <= nodel and noder <= right:
            self.minv[node] += incr
            self.maxv[node] += incr
            self.push[node] += incr
            return

        self._push(node)
        mid = (nodel + noder) // 2

        self._range_add(node * 2 + 1, nodel, mid, left, right, incr)
        self._range_add(node * 2 + 2, mid + 1, noder, left, right, incr)

        self.minv[node] = fmin(self.minv[node * 2 + 1], self.minv[node * 2 + 2])
        self.maxv[node] = fmax(self.maxv[node * 2 + 1], self.maxv[node * 2 + 2])

    def range_add(self, left, right, incr):
        self._range_add(0, 0, self.N - 1, left, right, incr)

    def _find_zero(self, node, nodel, noder):
        self._push(node)
        if self.minv[node] > 0 or self.maxv[node] < 0:
            return INF

        if nodel == noder:
            return nodel

        mid = (nodel + noder) // 2
        # if on the left
        if self.minv[node * 2 + 1] <= 0 <= self.maxv[node * 2 + 1]:
            return self._find_zero(node * 2 + 1, nodel, mid)
        else:
            return self._find_zero(node * 2 + 2, mid + 1, noder)


    def find_zero(self):
        return self._find_zero(0, 0, self.N - 1)

class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        N = len(nums)
        st = SegmentTree(N + 5)

        last_index = {}

        best = 0
        for index, x in enumerate(nums):
            delta = 1
            if x % 2 == 0:
                delta = -1

            # we want to modify all the prefix
            if x in last_index:
                st.range_add(last_index[x] + 1, index, delta)
            else:
                st.range_add(0, index, delta)
            findex = st.find_zero()
            last_index[x] = index

            if findex < index:
                best = max(best, index - findex + 1)
        return best







