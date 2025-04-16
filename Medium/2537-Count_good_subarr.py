# DQ 15 Apr 2025
# Sliding window
# Time - O(n)

class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        ans = 0
        left = 0
        count = defaultdict(int)
        pairs = 0
        for right in range(len(nums)):
            val = nums[right]
            pairs += count[val]
            count[val] += 1

            while pairs >= k:
                ans += len(nums) - right
                count[nums[left]] -= 1
                pairs -= count[nums[left]]
                left += 1

        return ans
