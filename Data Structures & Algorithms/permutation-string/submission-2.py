class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        mapS1, mapS2 = [0] * 26, [0] * 26
        matches = 0

        for i in range(len(s1)):
            mapS1[ord(s1[i]) - ord('a')] += 1
            mapS2[ord(s2[i]) - ord('a')] += 1

        for i in range(len(mapS1)):
            if mapS1[i] == mapS2[i]:
                matches += 1

        if matches == 26:
            return True

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            indexR = ord(s2[r]) - ord('a')
            indexL = ord(s2[l]) - ord('a')

            if mapS2[indexR] == mapS1[indexR]:
                matches -= 1
                mapS2[indexR] += 1
            else:
                mapS2[indexR] += 1
                if mapS2[indexR] == mapS1[indexR]:
                    matches += 1

            if mapS2[indexL] == mapS1[indexL]:
                matches -= 1
                mapS2[indexL] -= 1
                l += 1
            else:
                mapS2[indexL] -= 1
                if mapS2[indexL] == mapS1[indexL]:
                    matches += 1
                    l += 1
                else:
                    l += 1

            

        return matches == 26

