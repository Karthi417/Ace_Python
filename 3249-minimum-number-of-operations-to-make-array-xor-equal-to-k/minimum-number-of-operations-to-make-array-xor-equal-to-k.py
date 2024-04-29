class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        x=0
        for c in nums:
            x ^= c
        count=0
        for i in range(22):
            if((x & (1<<i))>0) != ((k & (1<<i))>0):
                count+=1
        return count