class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)
        L = [s2[i:i+n] for i in range(m - n + 1)]
        count = 0
        for elem in L:
            if sorted(elem) == sorted(s1):
                count += 1
            else:
                pass
        return count != 0

            