class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        checkSet = set()
        count = 1
        result = 0

        for num in nums:
            checkSet.add(num)


        for num in checkSet:
            count = 1
            if num-1 not in checkSet:
                while num+count in checkSet:
                    count += 1

                if count > result:
                    result = count

        return result
