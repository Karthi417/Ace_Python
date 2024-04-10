class Solution:
    def makeGood(self, s: str) -> str:
        q = []
        i = 0
        while i < len(s):
            if q and q[-1] != s[i] and q[-1].lower() == s[i].lower():
                q.pop()
            else:
                q.append(s[i])
            i += 1
        return "".join(q)