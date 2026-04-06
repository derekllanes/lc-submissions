class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res, l = 0, 0
        letMap = {}

        for r in range(len(s)):
            letMap[s[r]] = letMap.get(s[r], 0)+1

            while (r-l+1) - max(letMap.values()) > k:
                letMap[s[l]] = letMap.get(s[l])-1
                l += 1

            if (r-l+1) > res:
                res = (r-l+1)

        return res
