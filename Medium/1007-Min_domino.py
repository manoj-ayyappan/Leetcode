# DQ 3 May 2025
# Time - O(n)

class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        n = len(tops)
        candidates = set([tops[0], bottoms[0]])
        for t, b in zip(tops, bottoms):
            s2 = set([t, b])
            candidates = candidates.intersection(s2)
            if not candidates:
                return -1

        ans = n
        for c in candidates:
            t = tops.count(c)
            b = bottoms.count(c)
            ans = min(ans, min(n - t, t), min(n - b, b))

        return ans
