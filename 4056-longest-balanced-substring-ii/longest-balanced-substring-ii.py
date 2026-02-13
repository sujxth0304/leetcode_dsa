class Solution:
    def longestBalanced(self, s: str) -> int:
        N = len(s)

        # solves for "one character"
        def solve_one(s, c):
            streak = 0
            best = 0

            for x in s:
                if x == c:
                    streak += 1
                else:
                    streak = 0
                best = max(best, streak)
            return best

        def solve_two(s, a, b):
            current = 0
            # The first time we've seen a given delta prefix sum
            seen = {}
            best = 0
            seen[current] = 0

            for i in range(N):
                if s[i] not in [a, b]:
                    current = 0
                    seen = {}
                    seen[current] = i + 1
                    continue

                if s[i] == a:
                    current += 1
                elif s[i] == b:
                    current -= 1
                else:
                    assert(False)
                if current in seen:
                    best = max(best, i + 1 - seen[current])
                else:
                    seen[current] = i + 1
                
            return best

        def solve_three(s):
            # prefix delta of a - b
            ab = 0
            # prefix delta of a - c
            ac = 0
            seen = {}
            seen[(ab, ac)] = 0
            best = 0

            for i in range(N):
                if s[i] == "a":
                    ab += 1
                    ac += 1

                elif s[i] == "b":
                    ab -= 1
                else:
                    ac -= 1

                if (ab, ac) in seen:
                    best = max(best, i + 1 - seen[(ab, ac)])
                else:
                    seen[(ab, ac)] = i + 1
            return best

        best = 0
        for c in "abc":
            best = max(best, solve_one(s, c))
        for a, b in itertools.combinations("abc", 2):
            best = max(best, solve_two(s, a, b))
        best = max(best, solve_three(s))
        return best