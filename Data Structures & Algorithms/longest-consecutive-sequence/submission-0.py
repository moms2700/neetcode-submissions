from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        num_set = set(nums)  # Convert to set for O(1) lookups
        longest_streak = 0

        for num in num_set:
            if num - 1 not in num_set:  # Start of a new sequence
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:  # Continue counting the sequence
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)  # Update max length
        
        return longest_streak

