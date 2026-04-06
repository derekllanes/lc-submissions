class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1

        maxLeft = height[left]
        maxRight = height[right]

        total = 0

        while left < right:
            if maxLeft <= maxRight:
                left += 1
                check = maxLeft - height[left]
                if check > 0:
                    total += check
                if height[left] > maxLeft:
                    maxLeft = height[left]

            else:
                right -= 1
                check = maxRight - height[right]
                if check > 0:
                    total += check
                if height[right] > maxRight:
                    maxRight = height[right]

        return total
                    
                
                