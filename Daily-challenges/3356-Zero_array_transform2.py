# DQ 12 Mar 2025

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        # Brute force n^2

        # non_zero = 0
        # for x in nums:
        #     if x > 0:
        #         non_zero += 1
        
        # k = 1
        # for start, end, val in queries:
        #     for i in range(start, end+1):
        #         if nums[i] == 0:
        #             continue
        #         elif nums[i] - val <= 0:
        #             nums[i] = 0
        #             non_zero -= 1
        #         else:
        #             nums[i] -= val
        #     if non_zero == 0:
        #         return k
        #     k += 1
        # return -1

        n = len(nums)
        total = 0
        k = 0
        diff = [0] * (n + 1)
        for i in range(n):
            while total + diff[i] < nums[i]:
                k += 1
                if k > len(queries):
                    return -1
                left, right, val = queries[k - 1]
                if right >= i:
                    diff[max(left, i)] += val
                    if right + 1 < len(diff):
                        diff[right + 1] -= val
            total += diff[i]
        return k
