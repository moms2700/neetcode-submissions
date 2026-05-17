class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        memo = {}
        left = 0
        best = 0
        for right, ch in enumerate(s):
            if ch in memo and memo[ch] >= left:
                left = memo[ch] + 1
            memo[ch] = right
            best = max(best, right - left + 1)
        return best