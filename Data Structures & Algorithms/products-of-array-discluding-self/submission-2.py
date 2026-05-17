import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        L = []
        for i in range(len(nums)):
            produit = math.prod(nums[:i] + nums[i+1:])
            L.append(produit)
        return L