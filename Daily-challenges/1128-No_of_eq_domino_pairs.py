# DQ 3 May 2025

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        visit = defaultdict(int)
        for d in dominoes:
            if d[0] <= d[1]:
                visit[tuple(d)] += 1
            else:
                visit[(d[1], d[0])] += 1

        ans = 0
        for val in visit.values():
            ans += (val*(val-1) // 2)
        return ans
