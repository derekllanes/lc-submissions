class Solution:
    def isValid(self, s: str) -> bool:
        key = {')': '(', '}': '{', ']': '['}
        stack = []

        for tok in s:
            if not stack and tok in key.keys():
                return False
            elif stack and tok in key.keys():
                if stack.pop() != key[tok]:
                    return False
            elif tok in key.values():
                stack.append(tok)

        return not stack