class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        maxL = height[l]
        maxR = height[r]
        count, res = 0, 0


        while l < r:
            if maxL <= maxR:
                l += 1
                count = maxL - height[l]
                if count > 0:
                    res += count

                if height[l] > maxL:
                    maxL = height[l]

            else:
                r -= 1
                count = maxR - height[r]
                if count > 0:
                    res += count

                if height[r] > maxR:
                    maxR = height[r]

        return res