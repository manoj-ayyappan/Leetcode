# Unique paths 3

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        ans = 0
        visit = set()
        obstacles = set()
        empty = set()
        ROWS, COLS = len(grid), len(grid[0])
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    start_x, start_y = i, j
                elif grid[i][j] == 2:
                    end = (i, j)
                elif grid[i][j] == -1:
                    obstacles.add((i, j))
                else:
                    empty.add((i, j))
        empty.add((start_x, start_y))

        def backtrack(x, y):
            nonlocal ans
            if (
                (x, y) in visit or
                (x, y) in obstacles or
                x < 0 or x >= ROWS or
                y < 0 or y >= COLS
            ):
                return

            if (x, y) == end and visit == empty:
                ans += 1
                return

            visit.add((x, y))

            backtrack(x, y+1)
            backtrack(x, y-1)
            backtrack(x+1, y)
            backtrack(x-1, y)

            visit.remove((x, y))

        backtrack(start_x, start_y)
        return ans
