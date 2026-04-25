class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        if s == t:
            return True

        s_map, t_map = {}, {}
        for c in s:
            if c in s_map:
                s_map[c] += 1
            else:
                s_map[c] = 1 + s_map.get(c, 0)
        for c in t:
            if c in t_map:
                t_map[c] += 1
            else:
                t_map[c] = 1 + t_map.get(c, 0)
        return s_map == t_map