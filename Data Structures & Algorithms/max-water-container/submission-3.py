class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0

        l = 0
        r = len(heights)-1

        while l < r:
            if heights[l] > heights[r]:
                test = heights[r] * (r - l)
                if test > res:
                    res = test

                r -= 1

            else:
                test = heights[l] * (r - l)
                if test > res:
                    res = test

                l += 1

        return res