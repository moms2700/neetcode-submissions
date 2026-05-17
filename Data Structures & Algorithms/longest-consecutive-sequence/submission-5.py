class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        L = 1
        taille = 1
        nums = sorted(set(nums))
        for i in range(len(nums) -1):
            if nums[i+1] == nums[i] + 1:
                L += 1
                taille = max(L, taille)
            else : 
                L = 1
        return taille