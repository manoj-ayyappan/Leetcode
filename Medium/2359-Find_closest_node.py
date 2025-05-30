# DQ 29 May 2025

class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        # compute distance from a source node
        def helper(start):
            dist = [-1] * len(edges)
            visit = set()
            node = start
            distance = 0

            while node != -1 and node not in visit:
                dist[node] = distance
                visit.add(node)
                node = edges[node]
                distance += 1
            return dist

        dist1 = helper(node1)
        dist2 = helper(node2)

        min_dist = len(edges)
        idx = -1
        for i in range(len(edges)):
            if dist1[i] != -1 and dist2[i] != -1:
                max_dist = max(dist1[i], dist2[i])
                if max_dist < min_dist:
                    min_dist = max_dist
                    idx = i
                elif max_dist == min_dist and i < idx:
                    idx = i
        return idx
