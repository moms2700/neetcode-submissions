class Solution:
    def count(self, s: str):
        L = {} 
        for elem in set(s):
            L[elem] = s.count(elem) 
        return L
        
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False            
        return self.count(s) == self.count(t)