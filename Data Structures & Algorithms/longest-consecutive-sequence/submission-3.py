class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0

        for i, num in enumerate(nums):
            count = 1
            if num-1 not in nums:
                while num+count in nums:
                    count += 1

                res = max(res, count)

        return res