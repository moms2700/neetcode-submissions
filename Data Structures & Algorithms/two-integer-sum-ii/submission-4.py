class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        num = sorted(numbers)
        n = len(num)
        g, d = 0, n-1
        while g<d :
            if num[g]+num[d]<target:
                g += 1
            elif num[g]+num[d]>target:
                d -=1
            elif num[g]+num[d]==target:
                return [g+1,d+1]