class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        # Loop through
        # Slide the window
        for r, num in enumerate(nums):
            l = r-k+1
            if r >= k-1:
                res.append(max(nums[l:r+1]))
            

        return res
        
       
        
        