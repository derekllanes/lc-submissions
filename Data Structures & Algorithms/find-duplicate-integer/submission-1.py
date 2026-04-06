class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        check = [0] * (len(nums))

        for i, num in enumerate(nums):
            if check[nums[i]] > 0:
                return nums[i]
            else:
                check[nums[i]] += 1

        return 0
