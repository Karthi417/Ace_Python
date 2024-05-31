class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        res=set()
        for num in nums:
            if num not in res:
                res.add(num)
            else:
                res.remove(num)
        return list(res)
        