# DQ 13 Mar 2025
# Binary search

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        total = sum(candies)
        if total < k:
            return 0
        
        ans = 0
        l, r = 1, total // k

        while l <= r:
            m = (l + r) // 2
            count = 0
            for c in candies:
                if c >= m:
                    count += c // m
                if count >= k:
                    break
            if count >= k:
                ans = m
                l = m + 1
            else:
                r = m - 1
        
        return ans
