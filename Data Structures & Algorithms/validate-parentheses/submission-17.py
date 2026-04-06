class Solution:
    def isValid(self, s: str) -> bool:
        keyMap = {'}': '{', ']': '[', ')': '('}
        stack = []

        for char in s:
            if not stack and char in keyMap.keys():
                return False
            elif stack and char in keyMap.keys():
                if stack.pop() != keyMap.get(char):
                    return False
            elif char in keyMap.values():
                stack.append(char)
            

        return True if not stack else False
