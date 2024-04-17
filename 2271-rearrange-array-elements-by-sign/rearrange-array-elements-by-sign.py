class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        negindex=1
        posindex=0
        ans=[0]*n
        for i in range(n):
            if nums[i]<0:
                ans[negindex]=nums[i]
                negindex+=2
            else:
                ans[posindex]=nums[i]
                posindex+=2
        return ans