class Solution:
    def hammingWeight(self, n: int) -> int:
        c=0
        while n:
            if n&1:
                c+=1
            n=n>>1
        return c
        