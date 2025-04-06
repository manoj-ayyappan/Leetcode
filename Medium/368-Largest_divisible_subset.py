# DQ 5 Apr 2025
# DP solution
# Time - O(n^2)
# Space - O(n)

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        dp = [[n] for n in nums]
        ans = []
        for i in reversed(range(len(nums))):
            for j in range(i+1, len(nums)):
                if nums[j] % nums[i] == 0:
                    tmp = [nums[i]] + dp[j]
                    dp[i] = tmp if len(tmp) > len(dp[i]) else dp[i]
            ans = dp[i] if len(dp[i]) > len(ans) else ans
        return ans

        # Brute force
        # Time - O(n^2)
        # Space - O(n^2)

        # nums.sort()

        # @cache
        # def dfs(i, prev):
        #     # base case
        #     if i == len(nums):
        #         return []
        #     ans = dfs(i + 1, prev)  # skip nums[i]
        #     if nums[i] % prev == 0:
        #         tmp = [nums[i]] + dfs(i+1, nums[i]) # include nums[i]
        #         ans = tmp if len(tmp) > len(ans) else ans
        #     return ans

        # return dfs(0, 1)
