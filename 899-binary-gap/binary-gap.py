class Solution:
    def binaryGap(self, n: int) -> int:
        b = 30
        pos = []

        for i in range(b):
            if (n & (1 << i))>0:
                pos.append(i)

        
        best = 0
        for j in range(len(pos)-1):
            best = max(best, pos[j+1]-pos[j])
        return best