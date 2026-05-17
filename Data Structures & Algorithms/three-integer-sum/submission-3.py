class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        L = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            g, d = i+1, n-1
            while g < d:
                total = nums[i] + nums[g] + nums[d]
                if total < 0:
                    g += 1
                elif total > 0:
                    d -=1
                elif total == 0:
                    L.append([nums[i], nums[g], nums[d]]) 
                    while g < d and nums[g] == nums[g+1]:
                        g += 1
                    while g < d and nums[d] == nums[d-1]:
                        d -= 1
                    g += 1
                    d -= 1
        return L