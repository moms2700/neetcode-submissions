class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars = sorted(set(s))
        L1 = [s.count(m) for m in chars]
        L2 = [t.count(m) for m in chars]
        return L1==L2 and len(s)==len(t)
