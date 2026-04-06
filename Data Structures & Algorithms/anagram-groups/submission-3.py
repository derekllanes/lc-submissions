class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # word map of lists to store. key length of check list values grouped words
        wordMap = collections.defaultdict(list)

        for word in strs:
            wordLen = [0] * 26
            for let in word:
                wordLen[ord(let) - ord('a')] += 1

            wordMap[tuple(wordLen)].append(word)

        return list(wordMap.values())