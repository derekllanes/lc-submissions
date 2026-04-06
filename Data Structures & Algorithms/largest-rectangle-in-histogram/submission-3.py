class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0


        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                res = max(res, (i - index) * height)
                start = index

            stack.append((start, h))
        
        while stack:
            lastRect = stack.pop()
            res = max(res, (len(heights) - lastRect[0]) * lastRect[1])

        return res