# DQ 17 Mar 2025
# Sliding window
# Time - O(n)

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        mask, ans = 0, 0
        l = 0
        for r in range(len(nums)):
            while mask & nums[r] != 0:
                mask ^= nums[l]
                l += 1
            mask |= nums[r]
            ans = max(ans, r - l + 1)
        return ans
