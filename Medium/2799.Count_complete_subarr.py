# DQ 23 Apr 2025

class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        target = len(set(nums))
        n = len(nums)
        ans = 0
        for j in range(n - target + 1):
            seen = set()
            for i in range(j, n):
                if nums[i] not in seen:
                    seen.add(nums[i])
                    if len(seen) == target:
                        ans += (n - i)
                        break
        return ans
