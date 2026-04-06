class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        for i, num in enumerate(numbers):

            if target-num in numbers and numbers.index(target-num) != i:
                if numbers.index(target-num) < i:
                    return [int(numbers.index(target-num) + 1), i + 1]
                else:
                    return [i + 1, int(numbers.index(target-num) + 1)]

            