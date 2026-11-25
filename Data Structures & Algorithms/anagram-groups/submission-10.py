from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        casiers = {}
        for word in strs:
            lettres_triees = sorted(word)
            etiquette = "".join(lettres_triees)

            if etiquette not in casiers:
                casiers[etiquette] = []
            casiers[etiquette].append(word)

        return list(casiers.values())