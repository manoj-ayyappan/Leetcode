# DQ 9 Mar 2025
# Sliding window trick

class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        def atLeastK(k):
            vowels = {'a', 'e', 'i', 'o', 'u'}
            con, ans = 0, 0
            seen = Counter()
            left = 0

            for right in range(len(word)):
                if word[right] in vowels:
                    seen[word[right]] += 1
                else:
                    con += 1

                while len(seen) == 5 and con >= k:
                    ans += len(word) - right
                    if word[left] in vowels:
                        seen[word[left]] -= 1
                        if seen[word[left]] == 0:
                            del seen[word[left]]
                    else:
                        con -= 1
                    left += 1
            return ans

        return atLeastK(k) - atLeastK(k+1)
