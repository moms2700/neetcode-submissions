class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        L = {}
        num = set(nums)
        for elem in num:
            L[elem]= nums.count(elem)
        beta = sorted(L.items(), key=lambda item: item[1], reverse=True)
        z=[beta[i][0] for i in range(k)]
       
        return z






