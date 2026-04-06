class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res, l = 0, 0
        let = {}

        for r in range(len(s)):
            let[s[r]] = let.get(s[r], 0)+1

            while (r-l+1) - max(let.values()) > k:
                let[s[l]] = let[s[l]]-1
                l += 1

            if (r-l+1) > res:
                res = (r-l+1)

        return res
