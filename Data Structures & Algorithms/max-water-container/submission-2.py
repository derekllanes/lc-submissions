class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        count = 0

        left = 0
        right = len(heights)-1
        while left < right:
            if heights[left] > heights[right]:
                count = heights[right] * (right - left)
            else:
                count = heights[left] * (right - left)

            if count > res:
                res = count

            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
            

        return res
            

            