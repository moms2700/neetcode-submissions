class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        i,j = 0, n-1
        L = []
        for index, value in enumerate(nums): 
            L.append((value, index))  
        num = sorted(L)
        while i != j and i < j:
            somme = num[i][0] + num[j][0]
            if somme != target:
                if somme < target:
                    i += 1
                else:
                    j -= 1
            else:
                return [min(num[i][1], num[j][1]), max(num[i][1], num[j][1])]

        