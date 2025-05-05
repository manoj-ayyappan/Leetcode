# DQ 4 May 2025
# DP - saw hints in comments

class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10**9 + 7
        dp = [1] * (1001)
        dp[2] = 2
        dp[3] = 5
        for i in range(4, n+1):
            dp[i] = (dp[i-1] * 2 + dp[i-3]) % MOD
        return dp[n]
