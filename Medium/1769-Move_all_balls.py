# Time - O(n^2)
# Space - O(n)
# Should use prefix sum in ideal case for O(n)

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans = []
        for i in range(len(boxes)):
            count = 0
            for j in range(len(boxes)):
                if j == i or boxes[j] == '0':
                    continue
                count += abs(i-j)
            ans.append(count)
        return ans
