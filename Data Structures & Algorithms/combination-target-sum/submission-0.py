class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        resultats = []
        
        def dfs(index, current_subset, total_actuel):
            if total_actuel == target:
                resultats.append(current_subset[:])
                return
            
            if total_actuel > target or index >= len(nums):
                return

            current_subset.append(nums[index])
            
            dfs(index, current_subset, total_actuel + nums[index])           
            
            current_subset.pop()
            
            dfs(index + 1, current_subset, total_actuel)

        dfs(0, [], 0)
        return resultats