# DQ 4 Mar 2025
# Time - O(1)
# Space - O(1)

class Solution:
    def coloredCells(self, n: int) -> int:
        # Formula
        # 1 + 4(1 + 2 + 3....)
        # 1 + 4(n(n-1)/2)
        # 1 + 2*n*(n-1)
        return 1 + (2 * n * (n-1))
