class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers = {}
        
        for i, num in enumerate(nums):
            # check if i and j are the target
            if numbers and target - num in numbers.keys():
                # if so: return
                return [numbers[target-num], i]
            # if not: save move on
            else:
                numbers[num] = i

        return[0,0]