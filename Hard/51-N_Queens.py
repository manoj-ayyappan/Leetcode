# N Queens
# Time - O(n!)
# Space - O(n)

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        p_diag = set()  # (r+c)
        n_diag = set()  # (r-c)
        ans = []
        board = [["."] * n for _ in range(n)]

        def backtrack(r):
            # solution found
            if r == n:
                copy = ["".join(row) for row in board]
                ans.append(copy)
                return

            for c in range(n):
                if c in cols or (r+c) in p_diag or (r-c) in n_diag:
                    continue
                # use this config
                cols.add(c)
                p_diag.add(r+c)
                n_diag.add(r-c)
                board[r][c] = "Q"

                # backtrack
                backtrack(r+1)

                # undo this config
                cols.remove(c)
                p_diag.remove(r+c)
                n_diag.remove(r-c)
                board[r][c] = "."

        backtrack(0)
        return ans
