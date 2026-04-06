class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        right = len(numbers)-1
        for i, num in enumerate(numbers):

            if numbers[i] + numbers[right] > target:
                while numbers[i] + numbers[right] > target and i < right:
                    right -= 1
            
            if numbers[i] + numbers[right] == target:
                return [(i + 1), right+1]




            