# DQ 21 Apr 2025
# Prefix sum

class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        prefix = 0
        min_prefix = 0
        max_prefix = 0

        for d in differences:
            prefix += d
            min_prefix = min(min_prefix, prefix)
            max_prefix = max(max_prefix, prefix)

        return max(0, (upper - max_prefix) - (lower - min_prefix) + 1)
