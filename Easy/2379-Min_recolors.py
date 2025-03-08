# DQ 7 Mar 2025

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        # sliding window
        whites, blacks = 0, 0
        ans = float("inf")
        left = 0
        for right in range(len(blocks)):
            if blocks[right] == "W":
                whites += 1
            else:
                blacks += 1

            while right - left + 1 > k:
                if blocks[left] == "W":
                    whites -= 1
                else:
                    blacks -= 1
                left += 1

            if right - left + 1 == k:
                ans = min(ans, whites)
        return ans
