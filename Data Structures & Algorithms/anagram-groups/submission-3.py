class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        L = []
        used = []  
        for i, elem1 in enumerate(strs):
            if i not in used:
                group = [elem1]
                used.append(i)
                for j, elem2 in enumerate(strs):
                    if i != j and sorted(elem1) == sorted(elem2):
                        group.append(elem2)
                        used.append(j)
                L.append(group)
        return L