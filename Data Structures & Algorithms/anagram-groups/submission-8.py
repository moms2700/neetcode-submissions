class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)   

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        L = []
        for elem in strs:
            place_dans_un_groupe = False
            for groupe in L:
                if self.isAnagram(elem, groupe[0]):
                    groupe.append(elem)
                    place_dans_un_groupe = True
                    break
            if not place_dans_un_groupe:
                L.append([elem])  
        return L