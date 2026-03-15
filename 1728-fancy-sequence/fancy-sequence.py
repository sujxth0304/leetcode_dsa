MOD = 10 ** 9 + 7

class Fancy:
    def __init__(self):
        self.v = []
        self.a = 1
        self.b = 0

    def append(self, val: int) -> None:
        # v = (val - self.b) / self.a
        v = (val - self.b) * pow(self.a, -1, MOD)
        self.v.append(v)

    def addAll(self, inc: int) -> None:
        # we want to update self.f for all 0 to len(self.v)
        self.b += inc
        self.b %= MOD

    def multAll(self, m: int) -> None:
        self.a *= m
        self.b *= m
        self.a %= MOD
        self.b %= MOD

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.v):
            return -1

        return int(self.v[idx] * self.a + self.b) % MOD


# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)