class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        mapS = {}
        mapT = {}

        for x, y in zip(s, t):
            mapS[x] = mapS.get(x, 0) + 1
            mapT[y] = mapT.get(y, 0) + 1

        if mapS != mapT:
            return False

        return True