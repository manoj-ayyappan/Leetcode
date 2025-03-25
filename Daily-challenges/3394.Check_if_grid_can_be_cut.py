# DQ 24 Mar 2025
# Intervals
# Time - O(nlog(n))

class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        x = [(r[0], r[2]) for r in rectangles]  # (startx, endx)
        y = [(r[1], r[3]) for r in rectangles]  # (starty, endy)
        x.sort()
        y.sort()

        x_sections = 0
        prev_end = -1
        for start, end in x:
            if start >= prev_end:
                x_sections += 1
            prev_end = max(prev_end, end)

        y_sections = 0
        prev_end = -1
        for start, end in y:
            if start >= prev_end:
                y_sections += 1
            prev_end = max(prev_end, end)

        return max(x_sections, y_sections) >= 3
