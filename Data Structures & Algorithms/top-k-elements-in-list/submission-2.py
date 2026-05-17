class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        L = sorted(set(nums), key=nums.count, reverse=True)
        return L[:k]