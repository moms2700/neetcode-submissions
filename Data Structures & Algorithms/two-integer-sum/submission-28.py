class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        enum = [(num, i) for i, num in enumerate(nums)]
        num = sorted(enum, key=lambda x: x[0])
        i, j = 0, len(num) - 1
        while i != j:
            total = num[i][0] + num[j][0]
            if total < target:
                i += 1
            elif total > target:
                j -= 1
            else:
                return [min(num[i][1], num[j][1]), max(num[i][1], num[j][1])]
