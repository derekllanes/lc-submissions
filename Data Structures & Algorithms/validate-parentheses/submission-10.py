class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        if len(s) < 2:
            return False
        if s[0] in [")", "}", "]"]:
            return False

        for char in s:
            if char in "({[":
                stack.append(char)
            else:
                if len(stack) != 0:
                    compare = stack.pop()

                    if char == ")" and compare != "(":
                        return False
                    elif char == "}" and compare != "{":
                        return False
                    elif char == "]" and compare != "[":
                        return False
                else:
                    return False

        return len(stack) == 0
