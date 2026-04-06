class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        count = 1
        for i, num in enumerate(nums):
            res[i] *= count
            count *= num

        count = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= count
            count *= nums[i]

        return res