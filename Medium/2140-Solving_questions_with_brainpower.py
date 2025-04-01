# DQ 31 Mar 2025
# Backtrack, DP

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        @cache
        def backtrack(i):
            if i >= len(questions):
                return 0

            points, brainpower = questions[i]
            return max(
                backtrack(i + 1),   # skip
                points + backtrack(i + brainpower + 1)  # choose
            )
        return backtrack(0)
