class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        L = []
        n = len(nums)
        for i in range(n-k+1):
            L.append(max(nums[i:i+k]))
        return L