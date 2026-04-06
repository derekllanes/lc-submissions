class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        res = float('inf')

        # loop through nums
        while l <= r:
            m = (l+r) // 2

            # Check if sorted
            if nums[l] <= nums[r]:
                res = min(res, nums[l])


            # check if on left or right side
            
            # if on rightside, save then move left one
            if nums[l] > nums[m]:
                res = min(res, nums[m])
                r = m - 1
            else:
                # if on left side, move to right
                l = m + 1

        return res