# DQ 27 Apr 2025
# Time - O(n)
# Sliding window

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        left = 0
        window = 0

        for right in range(n):
            window += nums[right]
            while left <= right and window * (right - left + 1) >= k:
                window -= nums[left]
                left += 1
            ans += right - left + 1

        return ans
