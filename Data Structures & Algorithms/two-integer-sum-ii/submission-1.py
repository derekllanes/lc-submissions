class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        for i, num in enumerate(numbers):

            if numbers[i] + numbers[-1] > target:
                while numbers[i] + numbers[-1] > target:
                    numbers.pop()
            
            if numbers[i] + numbers[-1] == target:
                return [(i + 1), len(numbers)]




            