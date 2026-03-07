class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        n = len(s)
        start_one = False
        finish_one = False

        for c in s:
            if c == "1":
                if not start_one:
                    start_one = True

                elif finish_one:
                    return False
            else:
                if start_one:
                    finish_one = True
        return True