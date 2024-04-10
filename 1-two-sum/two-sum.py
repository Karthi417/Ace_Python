class Solution:
    def twoSum(self,nums,target):
        hasht={}
        for i,n in enumerate(nums):
            diff=target-n
            if diff in hasht:
                return [hasht[diff],i]
            hasht[n]=i
        return 
            

        
        