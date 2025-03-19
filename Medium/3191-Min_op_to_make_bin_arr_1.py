# DQ 18 Mar 2025
# Time - O(n)

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)-2):
            if nums[i] == 0:
                ans += 1
                nums[i] = 1
                nums[i+1] ^= 1
                nums[i+2] ^= 1

        return ans if nums[-1] == nums[-2] == 1 else -1
