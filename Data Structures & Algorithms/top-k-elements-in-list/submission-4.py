class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num = list(set(nums))
        L = [nums.count(x) for x in num]
        fin = [[num[i], L[i]] for i in range(len(L))]
        fin.sort(key=lambda x: x[1], reverse=True)  
        beta = list(fin[:k])  
        z = [beta[i][0] for i in range(len(beta))]
        return z