class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if set(s) == set(t) and len(s) == len(t):
            if [s.count(elem) for elem in sorted(set(s))] == [t.count(elem) for elem in sorted(set(t))]:
                return True
        return False