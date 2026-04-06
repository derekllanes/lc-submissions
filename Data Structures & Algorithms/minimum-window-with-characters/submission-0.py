class Solution:
    def minWindow(self, s: str, t: str) -> str:
        haveMap, needMap = {}, {}
        cond = 0
        res, resLen = (), float("inf")

        for let in t:
            haveMap[let] = 0
            needMap[let] = needMap.get(let, 0)+1

        l = 0

        for r in range(len(s)):
            if s[r] in needMap:
                haveMap[s[r]] += 1
                if haveMap[s[r]] == needMap[s[r]]:
                    cond += 1
                    while cond == len(needMap):
                        if r-l+1 < resLen:
                            res = (l, r)
                            resLen = r-l+1

                        if s[l] in needMap:
                            haveMap[s[l]] -= 1
                            if haveMap[s[l]] < needMap[s[l]]:
                                cond -= 1

                        l += 1

        if resLen != float('inf'):
            l, r = res
            return s[l:r+1]
        else:
            return ""
