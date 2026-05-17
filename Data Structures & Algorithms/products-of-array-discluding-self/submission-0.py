from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        L = []  # Output list
        
        for i in range(len(nums)):  # Iterate over each index
            product = 1  # Reset product for each i
            
            for j in range(len(nums)):  # Multiply all elements except nums[i]
                if i != j:
                    product *= nums[j]  
                    
            L.append(product)  # Store the computed product
        
        return L
