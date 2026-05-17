class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = ''.join(c.lower() for c in s if c.isalnum())
        n = len(result)
        for i in range(n // 2):
            if result[i] != result[n - i - 1]:
                return False
        return True