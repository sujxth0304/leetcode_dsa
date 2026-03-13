class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        left = 1
        right = 10 ** 20

        # workerTimes[i] * (1 + 2 + 3 + ... + x) == target
        # workerTimes[i] * (x * (x + 1)) // 2 == target
        # (x * (x + 1)) == target * 2 / workerTimes[i]
        # x^2 + x - target * 2 / workerTimes[i] = 0

        # a = 1
        # b = 1
        # c = -target * 2 / workerTimes[i] 

        # -b +- sqrt(b^2 - 4ac)
        # ---------------------
        #         2a

        def f(target, t):
            left = 0
            right = 10 ** 20

            for _ in range(1000):
                mid = (left + right) / 2

                if (mid * (mid + 1)) // 2 * t <= target:
                    left = mid
                else:
                    right = mid
            return left


        # target satisfies the condition
        # given "target" seconds, all the mountainHeight is used
        def good(target):
            removed = 0

            a = 1
            b = 1
            for t in workerTimes:
                c = -target * 2 / t
                s = sqrt(b * b - 4 * a * c)

                x = (-b + s) / (2 * a)
                if x >= 0:
                    removed += int(x)
                else:
                    x = (-b - s) / (2 * a)
                    removed += int(x)

                """
                x2 = f(target, t)
                removed += int(x2)
                #print(t, x, x2)
                """

            #print(target, removed)
            return removed >= mountainHeight

        while left < right:
            mid = (left + right) // 2

            if good(mid):
                right = mid
            else:
                left = mid + 1

        return left