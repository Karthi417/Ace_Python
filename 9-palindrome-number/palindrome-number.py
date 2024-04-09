class Solution:
    def isPalindrome(self, x: int) -> bool:
        res=0
        dup=x
        while x>0:
            lst_dig= x%10
            res= res*10 + lst_dig
            x=x//10
        if (dup==res): return True
        else: return False
        