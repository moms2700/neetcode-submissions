class Solution:
    def product(self, nums):
        result = 1
        for x in nums:
            result *= x
        return result
        
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        L = []
        for i in range(len(nums)):
            L.append(self.product(nums[:i] + nums[i+1:]))
        return L