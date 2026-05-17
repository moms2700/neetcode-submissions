class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        num = sorted(set(nums))  
        j = 1  
        L = []
        for i in range(len(num) - 1):
            if num[i+1] == num[i] + 1:
                j += 1
            else:
                L.append(j)
                j = 1 
        L.append(j)  
        return max(L)