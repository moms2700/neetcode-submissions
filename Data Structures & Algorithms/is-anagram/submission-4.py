from typing import List

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        a, b = sorted(s), sorted(t)  # Trie les deux chaînes

        for i in range(len(a)):  # Compare chaque caractère trié
            if a[i] != b[i]:
                return False

        return True