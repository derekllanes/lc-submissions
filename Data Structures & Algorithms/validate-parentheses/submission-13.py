class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        if len(s) < 2:
            return False
        if s[0] in [")", "}", "]"]:
            return False


        for char in s:
            if char == "(" or char == "{" or char == "[":
                stack.append(char)
            else:
                if len(stack) != 0:
                    compare = stack.pop()

                    if char == ")":
                        if compare != "(":
                            return False
                    elif char == "}":
                        if compare != "{":
                            return False
                    else:
                        if compare != "[":
                            return False
                else:
                    return False


        return len(stack) == 0
