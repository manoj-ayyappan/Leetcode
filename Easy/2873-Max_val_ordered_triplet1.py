# DQ 1 Apr 2025
# Time - O(1)

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        maxTriplet, maxElement, maxDiff = 0, 0, 0
        for num in nums:
            maxTriplet = max(maxTriplet, maxDiff * num)
            maxDiff = max(maxDiff, maxElement - num)
            maxElement = max(maxElement, num)
        return maxTriplet
