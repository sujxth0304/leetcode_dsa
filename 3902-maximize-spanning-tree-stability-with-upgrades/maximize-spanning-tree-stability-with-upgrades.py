class Solution:
    def maxStability(self, N: int, edges: List[List[int]], k: int) -> int:
        # Minimum Spanning Tree
        # Union-Find

        parents = [x for x in range(N)]
        def ufind(x):
            if parents[x] != x:
                parents[x] = ufind(parents[x])
            return parents[x]

        # return whether we used this edge
        def uunion(a, b):
            ua = ufind(a)
            ub = ufind(b)

            if ua != ub:
                parents[ua] = ub
                return True
            return False

        weights = []
        used = 0
        def add(u, v, s):
            if uunion(u, v):
                nonlocal used
                used += 1
                return True
            return False


        consider = []
        for u, v, s, m in edges:
            if m == 1:
                if not add(u, v, s): # no choice
                    return -1
                weights.append(s)
            else:
                consider.append((u, v, s))

        consider.sort(key=lambda x: -x[2])
        # for a tree with N nodes, we want N - 1 things

        upgrade_weights = []
        for u, v, s in consider:
            if add(u, v, s):
                upgrade_weights.append(s)

        if used != N - 1:
            return -1

        upgrade_weights.sort()
        for i in range(min(k, len(upgrade_weights))):
            upgrade_weights[i] *= 2

        weights.extend(upgrade_weights)
        return min(weights)