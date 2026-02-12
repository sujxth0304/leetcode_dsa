class Solution:
    def longestBalanced(self, s: str) -> int:
        max_sub = 0
        for i in range(len(s)):
            count = {}
            unique = 0
            maximum = 0
            for j in range(i, len(s)):
                if s[j] not in count:
                    count[s[j]] = 1 + count.get(s[j], 0)
                else:
                    count[s[j]] += 1

                if count[s[j]] == 1:
                    unique += 1
                
                if count[s[j]] > maximum:
                    maximum = count[s[j]]

                length = j - i + 1
                if maximum*unique == length:
                    if length> max_sub:
                        max_sub = length
        return max_sub



                
