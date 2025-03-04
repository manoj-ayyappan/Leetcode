# DQ 3 Mar 2025
# Time - O(logn)
# Space - O(1)

class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n > 0:
            if n % 3 == 2:
                return False
            n //= 3

        return True
