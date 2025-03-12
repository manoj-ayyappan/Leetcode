# Binary search

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        pos_start = 0
        pos_end = 0
        neg_end = 0
        pos, neg = 0, 0

        if nums[0] == nums[-1] == 0:
            return 0

        # find neg_end
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r-l) // 2
            if nums[mid] < 0:
                neg_end = mid
                l = mid + 1
            else:
                r = mid - 1

        # find pos_start
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r-l) // 2
            if nums[mid] > 0:
                pos_start = mid
                r = mid - 1
            else:
                l = mid + 1

        if nums[-1] > 0:
            pos_end = len(nums) - 1

        pos = pos_end - pos_start + 1
        neg = neg_end + 1

        return max(pos, neg)
