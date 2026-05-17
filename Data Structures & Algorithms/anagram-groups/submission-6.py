class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if set(s) == set(t) and len(s) == len(t):
            if [s.count(elem) for elem in sorted(set(s))] == [t.count(elem) for elem in sorted(set(t))]:
                return True
        return False
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        L = []
        used = set()
        for i, elem in enumerate(strs):
            if i in used:
                continue
            group = [elem]
            for j, x in enumerate(strs):
                if i != j and self.isAnagram(elem, x):
                    group.append(x)
                    used.add(j)
            L.append(group)
        return L