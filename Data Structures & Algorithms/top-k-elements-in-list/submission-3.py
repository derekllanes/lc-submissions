class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        res = []

        for num in nums:
            count[num] = count.get(num, 0)+1

        freq = [[] for i in range(len(nums)+1)]

        for i, c in count.items():
            freq[c].append(i)

        for j in range(len(freq)-1, 0, -1):
            for num in freq[j]:
                res.append(num)
                if len(res) == k:
                    return res
