class Solution:
    def isPalindrome(self, s: str) -> bool:
        # pointer at beggining 
        # pointer at end
        l, r = 0, len(s)-1
        # compare characters
        while l < r:
            # if true by the time they meet then true
            if not s[l].isalnum():
                l += 1
            elif not s[r].isalnum():
                r -= 1
            elif s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            # if false at any time then false
            else:
                return False

        return True
