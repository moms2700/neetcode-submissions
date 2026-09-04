class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nu = sorted(enumerate(nums), key=lambda x: x[1])        
        i, j = 0, len(nu) - 1
        
        while i < j:
            # On vérifie la somme sur le tableau trié !
            somme = nu[i][1] + nu[j][1]
            
            if somme < target:
                i += 1
            elif somme > target:
                j -= 1
            else:
                return sorted([nu[i][0], nu[j][0]])
                
        # Sécurité pour le compilateur
        return []