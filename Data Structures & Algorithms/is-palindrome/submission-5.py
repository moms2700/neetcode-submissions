class Solution:
    def isPalindrome(self, s: str) -> bool:
        se = "".join(ch.lower() for ch in s if ch.isalnum())
        n = len(se)
        for i in range(n):
            if set(se[i]) != set(se[n-1-i]):
                return False
        return True