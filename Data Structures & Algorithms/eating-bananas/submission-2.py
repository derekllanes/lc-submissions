class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L, R = 1, max(piles)
        
        while L <= R:
            k = (R + L) // 2
            total = 0

            for p in piles:
                total += math.ceil(p / k)

            if total <= h:
                R = k - 1
                res = k
            else:
                L = k + 1

        return res
            
