class Solution:
    def isPalindrome(self, s: str) -> bool:
        a=''.join(char for char in s if char.isalnum())
        return True if a.lower()==a.lower()[::-1] else False

        