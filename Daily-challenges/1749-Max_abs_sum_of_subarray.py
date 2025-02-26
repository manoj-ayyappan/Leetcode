# 25 Feb 2025
# Time - O(n)
# Space - O(1)

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        # max absolute sum will be either the max sum or the min sum
        curMax = 0
        totalMax = float('-inf')
        curMin = 0
        totalMin = float('inf')

        for i in range(len(nums)):
            a = curMax + nums[i]
            totalMax = max(a, nums[i], totalMax)
            curMax = max(a, nums[i])

            b = curMin + nums[i]
            totalMin = min(b, nums[i], totalMin)
            curMin = min(b, nums[i])

        return max(abs(totalMin), totalMax)
