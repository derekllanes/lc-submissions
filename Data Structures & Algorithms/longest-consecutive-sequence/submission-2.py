class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0

        for num in nums:
            if num-1 not in nums:
                count = 1
                while num+count in nums:
                    count += 1
                if count > res:
                    res = count

        return res
