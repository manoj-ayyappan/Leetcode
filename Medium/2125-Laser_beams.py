# time - O(2n)

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        beams = []
        for l in bank:
            if l.count("1") != 0:
                beams.append(l.count("1"))
        ans = 0
        for x, y in pairwise(beams):
            ans += x * y

        return ans
