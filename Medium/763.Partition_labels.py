# DQ 29 Mar 2025
# Time - O(n)
# Space - O(1)

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = [-1] * 26
        for i in range(len(s) - 1, -1, -1):
            if last[ord(s[i]) - ord('a')] == -1:
                last[ord(s[i]) - ord('a')] = i

        ans = []
        start, end = 0, 0
        for i, char in enumerate(s):
            end = max(end, last[ord(char) - ord('a')])
            if i == end:
                size = i - start + 1
                ans.append(size)
                start = i + 1
        return ans
