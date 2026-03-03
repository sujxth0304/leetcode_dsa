class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        k -= 1
        def f(n, k):
            if n ==1:
                return 0
            if k < pow(2, n-1)-1:
                return f(n-1, k)

            k -= pow(2, n-1)-1

            if k ==0:
                return 1
            k-=1

            return 1 - f(n-1, pow(2, n-1)-1-k-1)
        return str(f(n, k))
