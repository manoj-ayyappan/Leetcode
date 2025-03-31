# DQ 31 Mar 2025
# Time - O(nlogn)

class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        n = len(weights)
        if k == 1 or k == n:
            return 0

        pair_sums = []
        for i in range(n - 1):
            pair_sums.append(weights[i] + weights[i+1])

        pair_sums.sort()

        min_score = sum(pair_sums[:k-1])
        max_score = sum(pair_sums[-(k-1):])

        return max_score - min_score
