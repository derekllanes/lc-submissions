class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}

        for i, num in enumerate(numbers):
            if not seen:
                seen[num] = i+1
                continue

            if (target - num) in seen.keys():
                return [seen[target-num], i+1]
            else:
                seen[num] = i+1