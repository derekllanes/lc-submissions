class Solution:
    def isPalindrome(self, s: str) -> bool:
        leftLet = 0
        rightLet = len(s) - 1

        while leftLet < rightLet:
            while leftLet < rightLet and not s[leftLet].isalnum():
                leftLet += 1
            while leftLet < rightLet and not s[rightLet].isalnum():
                rightLet -= 1

            if s[leftLet].lower() != s[rightLet].lower():
                return False

            leftLet += 1
            rightLet -= 1

        return True