# Time - O(n)
# Space - O(n)

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        ans = []
        buckets = defaultdict(list)

        for i, s in enumerate(groupSizes):
            buckets[s].append(i)
            if len(buckets[s]) == s:
                ans.append(buckets[s])
                buckets[s] = []
        return ans
