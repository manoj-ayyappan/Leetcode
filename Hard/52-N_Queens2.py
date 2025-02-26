# N Queens 2
# Time - O(n!)
# Space - O(n)

class Solution:
    def totalNQueens(self, n: int) -> int:
        ans = 0
        cols = set()
        p_diag = set()
        n_diag = set()

        def backtrack(r):
            if r == n:
                nonlocal ans
                ans += 1
                return

            for c in range(n):
                if c in cols or (r+c) in p_diag or (r-c) in n_diag:
                    continue

                cols.add(c)
                p_diag.add(r+c)
                n_diag.add(r-c)

                backtrack(r + 1)

                cols.remove(c)
                p_diag.remove(r+c)
                n_diag.remove(r-c)

        backtrack(0)
        return ans
