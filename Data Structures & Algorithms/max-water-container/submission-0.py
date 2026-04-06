class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        count = 0

        for i, num in enumerate(heights):
            right = len(heights)-1
            while i < right:
                if heights[i] > heights[right]:
                    count = heights[right] * (right - i)
                else:
                    count = heights[i] * (right - i)

                if count > res:
                    res = count

                right -= 1
            

        return res
            

            