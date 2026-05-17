from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string."""
        return ''.join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string back into a list of strings."""
        res = []
        i = 0
        
        while i < len(s):
            j = i
            while s[j] != "#":  # Find the separator
                j += 1
            length = int(s[i:j])  # Extract length
            i = j + 1  # Move past "#"
            res.append(s[i:i+length])  # Extract string
            i += length  # Move to next encoded string
        
        return res