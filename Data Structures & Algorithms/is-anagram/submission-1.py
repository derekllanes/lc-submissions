class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        lettersS = {}
        lettersT = {}

        for s, t in zip(s, t):
            lettersS[s] = lettersS.get(s, 0) + 1
            lettersT[t] = lettersT.get(t, 0) + 1

        if lettersS == lettersT:
            return True

        return False
