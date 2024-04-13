class Solution:
    def check(self, nums: List[int]) -> bool:
        sorted_arr=sorted(nums)
        for i in range(len(nums)):
            rotated_arr=nums[i:]+nums[:i]
            if rotated_arr==sorted_arr:
                return True
        return False

        