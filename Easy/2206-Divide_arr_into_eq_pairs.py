# DQ 16 Mar 2025
# Time - O(1)

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        ans = 0
        for n in nums:
            ans ^= (1 << n)
        return ans == 0

        # Loop - hashmap
        # count = Counter(nums)
        # for c in count.values():
        #     if c % 2 != 0:
        #         return False
        # return True
