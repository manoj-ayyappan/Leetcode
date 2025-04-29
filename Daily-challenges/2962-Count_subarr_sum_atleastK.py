# DQ 28 Apr 2025
# Sliding window

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        key = max(nums)
        n = len(nums)
        left = 0
        ans = 0
        count = 0
        for right in range(n):
            if nums[right] == key:
                count += 1

            while count >= k:
                if nums[left] == key:
                    count -= 1
                left += 1
            ans += left
        return ans
