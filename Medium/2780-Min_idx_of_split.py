# DQ 26 Mar 2025
# Time - O(n)
# find the mode and its count

class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        freq = Counter(nums)
        n = len(nums)
        dom, total = 0, 0

        for num, c in freq.items():
            if c > n // 2:
                dom, total = num, c
                break

        count = 0
        for i in range(n):
            if nums[i] == dom:
                count += 1
            if count > (i+1)//2 and (total - count) > (n - (i+1))//2:
                return i
        return -1
