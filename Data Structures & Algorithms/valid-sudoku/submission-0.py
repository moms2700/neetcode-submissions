from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]  # Each 3x3 box

        for r in range(9):
            for c in range(9):
                num = board[r][c]

                if num == ".":
                    continue  # Skip empty cells

                box_index = (r // 3) * 3 + (c // 3)  # Compute 3x3 box index

                if num in rows[r] or num in cols[c] or num in boxes[box_index]:
                    return False  # Found duplicate in row, column, or box

                # Add number to row, column, and box
                rows[r].add(num)
                cols[c].add(num)
                boxes[box_index].add(num)
        return True  # No duplicates found