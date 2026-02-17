class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        def count(x):
            return bin(x)[2:].count("1")


        ans = []
        for hh in range(12):
            for mm in range(60):
                if count(hh) + count(mm) == turnedOn:
                    ans.append(f"{hh}:{mm:02}")
        return ans