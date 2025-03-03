# DQ 2 Mar 2025
# Time - O(n)
# Space - O(n)

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less, eq, more = [], [], []
        for n in nums:
            if n < pivot:
                less.append(n)
            elif n == pivot:
                eq.append(n)
            else:
                more.append(n)

        return less + eq + more
