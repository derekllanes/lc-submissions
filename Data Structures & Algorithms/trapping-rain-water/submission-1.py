class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        left = 0
        right = len(height)-1
        count = 0

        maxLeft = height[left]
        maxRight = height[right]

        while left < right:
            if maxLeft <= maxRight:
                left += 1
                count = maxLeft - height[left]
                if count > 0:
                    total += count
                if height[left] > maxLeft:
                    maxLeft = height[left]
                

            else:
                right -= 1
                count = maxRight - height[right]
                if count > 0:
                    total += count
                if height[right] > maxRight:
                    maxRight = height[right]
                

        return total
