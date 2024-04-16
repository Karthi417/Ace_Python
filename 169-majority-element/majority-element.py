class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt=0
        el=0
        for num in nums:
            if cnt==0:
                el=num
            if num==el:
                cnt+=1
            else:
                cnt-=1
        return el
        
        