class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        results = {}

        for i, num in enumerate(nums):
            if target - num in results:
                return [results[target-num], i]

            results[num] = i