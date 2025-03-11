# DQ 10 Mar 2025
# simple sliding window

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        ans = 0
        seen = Counter()
        l = 0
        for r in range(len(s)):
            if s[r] in "abc":
                seen[s[r]] += 1
            while len(seen) == 3:
                ans += len(s) - r
                seen[s[l]] -= 1
                if seen[s[l]] == 0:
                    del seen[s[l]]
                l += 1
        return ans
