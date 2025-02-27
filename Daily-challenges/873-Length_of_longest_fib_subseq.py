# DQ 27 Feb 2025
# Time - Lesser tha O(n^3)
# Greedy

class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        ans = 0
        hashset = set(arr)

        for i in range(len(arr)-1):
            for j in range(i+1, len(arr)):
                prev, cur = arr[i], arr[j]
                nxt = prev + cur
                count = 2

                while nxt in hashset:
                    count += 1
                    prev, cur = cur, nxt
                    nxt = prev + cur
                    ans = max(count, ans)
        return ans

# Dp solution


class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        ans = 0
        hashmap = {n: i for i, n in enumerate(arr)}
        dp = {}

        for i in reversed(range(len(arr)-1)):
            for j in reversed(range(i+1, len(arr))):
                prev, cur = arr[i], arr[j]
                nxt = prev + cur
                count = 2

                if nxt in hashmap:
                    count = 1 + dp[j, hashmap[nxt]]
                    ans = max(count, ans)
                dp[(i, j)] = count
        return ans
