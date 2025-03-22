# DQ 21 Mar 2025
# Union find algo

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if x != y:
            if self.rank[x] < self.rank[y]:
                self.parent[x] = y
                self.rank[y] += self.rank[x]
            else:
                self.parent[y] = x
                self.rank[x] += self.rank[y]


class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        # Build components
        uf = UnionFind(n)
        for u, v in edges:
            uf.union(u, v)

        comp_size = [0] * n
        comp_edges = [0] * n

        for i in range(n):
            comp_size[uf.find(i)] += 1

        for u, v in edges:
            comp_edges[uf.find(u)] += 1

        ans = 0
        for i in range(n):
            if uf.find(i) == i:
                # no of edges for complete graph = n(n-1)/2
                if comp_edges[i] == (comp_size[i] * (comp_size[i] - 1)) / 2:
                    ans += 1

        return ans
