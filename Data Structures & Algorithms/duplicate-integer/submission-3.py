from collections import Counter

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        b = 0
        n = len(nums)
        for elem in nums:
            if nums.count(elem) == 1:
                b += 1
        if b == n :
            return False
        else:
            return True
            
            
        
        