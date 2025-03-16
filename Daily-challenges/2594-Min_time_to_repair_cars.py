# DQ 15 Mar 2025
# Binary search

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        ranks = Counter(ranks)

        def isValid(time):
            cars_done = 0
            for rank, workers in ranks.items():
                cars_done += workers * floor(sqrt(time/rank))
            return cars_done >= cars

        ans = 0
        l, r = 0, max(ranks) * ceil(cars/len(ranks)) ** 2
        while l <= r:
            m = (l + r) // 2
            if isValid(m):
                ans = m
                r = m - 1
            else:
                l = m + 1

        return ans
