from functools import reduce

class Solution:
    def makeGood(self, s: str) -> str:
        return reduce(lambda x, y: x[:-1] if x and x[-1] != y and x[-1].lower() == y.lower() else x + y, s, "")
