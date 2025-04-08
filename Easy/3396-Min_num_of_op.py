class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        seen = set()
        for i in reversed(range(len(nums))):
            if nums[i] not in seen:
                seen.add(nums[i])
            else:
                return ceil((i+1) / 3)
        return 0
