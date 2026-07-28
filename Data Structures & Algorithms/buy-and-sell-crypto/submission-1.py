class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Start and both ends
        # if left is larger than right: Dont buy
        #   reset right
        #   move right pointer in
        #   loop
        # left is larger than right: Buy and track
        #   left - right 
        #   bigger than current max? 
        #   left in

        res = 0

        for l in range(len(prices)):
            r = len(prices)-1
            while l < r:
                if prices[l] <= prices[r]:
                    res = max(res, prices[r] - prices[l])

                r -= 1

        return res

            
            
