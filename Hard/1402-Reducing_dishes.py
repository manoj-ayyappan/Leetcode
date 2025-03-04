# Greedy approach
# Time - O(nlogn)
# Space = O(1)

class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        ans, total = 0, 0
        while satisfaction and satisfaction[-1] + total > 0:
            total += satisfaction.pop()
            ans += total
        return ans
