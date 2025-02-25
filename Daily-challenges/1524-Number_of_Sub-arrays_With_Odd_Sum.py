# 24 Feb 2025
# Time - O(n)
# Space - O(1)

class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        count, prefix = 0, 0
        even_count, odd_count = 1, 0    # initial sum 0 is even
        for x in arr:
            prefix += x
            if prefix % 2 == 0:
                count += odd_count
                even_count += 1
            else:
                count += even_count
                odd_count += 1
            count %= MOD
        return count
