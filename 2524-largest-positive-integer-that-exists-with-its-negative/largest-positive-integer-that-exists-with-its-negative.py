class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        a=set(nums)

        best=-1
        for k in nums:
            if k>0 and -k in a:
                best=max(best,k)
        return best