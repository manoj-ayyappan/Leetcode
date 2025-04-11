# DQ 10 Apr 2025
# Brute force O(n^2)

class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        ans = 0
        for n in range(low, high+1):
            x = str(n)
            if len(x) % 2 == 0:
                half = len(x) // 2
                lsum = sum(int(x[i]) for i in range(half))
                rsum = sum(int(x[i]) for i in range(half, len(x)))
                if lsum == rsum:
                    ans += 1
        return ans
