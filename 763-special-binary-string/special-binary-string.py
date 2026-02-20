class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        INF = 10 ** 20

        N = len(s)

        @cache
        # left to right inclusive
        def f(left, right):
            if left > right:
                return 0
            # this has to be a prefix of 1, 
            # otherwise we do not have a special 
            # binary string as an input, and we are crazy
            if s[left] == "0" or s[right] == "1":
                return -INF

            best = f(left + 1, right - 1) * 2 + (1 << (right - left))

            # figure out swaps in a greedy way (???)
            chunks = []

            current = 0
            start = left
            for i in range(left, right + 1):
                if s[i] == "1":
                    current += 1
                else:
                    current -= 1

                if current < 0:
                    # not a special string
                    return best
                if current == 0:
                    if start == left and i == right:
                        # there is only one chunk, so no mas
                        chunks.append((int(s[left:right + 1], 2), right - left + 1))
                    else:
                        chunks.append((f(start, i), i - start + 1))

                    start = i + 1

            chunks.sort(key=lambda x: bin(x[0]), reverse=True)
            r = 0
            for x, L in chunks:
                r <<= L
                r += x
            best = max(best, r)
            return best
        return bin(f(0, N - 1))[2:]