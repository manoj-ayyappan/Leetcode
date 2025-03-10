# Time - O(n)

class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        ans = s.split()
        return " ".join(ans[:k])
