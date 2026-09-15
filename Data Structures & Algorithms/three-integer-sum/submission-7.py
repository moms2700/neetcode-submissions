class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        L = []
        n = len(nums)
        
        for k in range(n - 2):
            # Éviter les doublons pour le premier nombre (k)
            if k > 0 and nums[k] == nums[k-1]:
                continue
                
            i = k + 1
            j = n - 1
            
            while i < j:
                total = nums[k] + nums[i] + nums[j]
                
                if total < 0:
                    i += 1
                elif total > 0:
                    j -= 1
                else:
                    L.append([nums[k], nums[i], nums[j]])
                    
                    # Ignorer les doublons pour i
                    while i < j and nums[i] == nums[i + 1]:
                        i += 1
                    # Ignorer les doublons pour j
                    while i < j and nums[j] == nums[j - 1]:
                        j -= 1
                        
                    # Avancer les pointeurs pour chercher de nouvelles combinaisons
                    i += 1
                    j -= 1
                    
        return L