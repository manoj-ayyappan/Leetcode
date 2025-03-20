# DQ 19 Mar 2025
# Union find
# Time - O(E + q)

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x != y:
            if self.size[x] < self.size[y]:
                self.parent[x] = y
                self.size[y] += self.size[x]
            else:
                self.parent[y] = x
                self.size[x] += self.size[y]


class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        # 1. Build components
        uf = UnionFind(n)
        for u, v, w in edges:
            uf.union(u, v)

        # 2. Get cost of each component
        component_cost = {}  # root -> cost
        for u, v, w in edges:
            root = uf.find(u)
            if root not in component_cost:
                component_cost[root] = w
            else:
                component_cost[root] &= w

        # 3. Queries
        ans = []
        for src, dst in query:
            r1, r2 = uf.find(src), uf.find(dst)
            if r1 != r2:
                ans.append(-1)
            else:
                ans.append(component_cost[r1])
        return ans
