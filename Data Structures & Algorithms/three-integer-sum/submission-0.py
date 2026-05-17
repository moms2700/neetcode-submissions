from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Sorting helps avoid duplicates and use two-pointer technique
        L = []
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicate values for `i`
                continue

            left, right = i + 1, len(nums) - 1  # Two pointers
            
            while left < right:
                three_sum = nums[i] + nums[left] + nums[right]
                
                if three_sum == 0:
                    L.append([nums[i], nums[left], nums[right]])
                    
                    # Move left and right to skip duplicates
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
                
                elif three_sum < 0:
                    left += 1  # Increase sum by moving `left`
                else:
                    right -= 1  # Decrease sum by moving `right`
        
        return L