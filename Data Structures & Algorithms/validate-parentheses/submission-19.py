class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for tok in s:
            if stack:
                if tok == ')':
                    if stack.pop() != '(':
                        return False
                elif tok == '}':
                    if stack.pop() != '{':
                        return False
                elif tok == ']':
                    if stack.pop() != '[':
                        return False
                else:
                    stack.append(tok)
            elif not stack:
                if tok in [')', '}', ']']:
                    return False
                else:
                    stack.append(tok)

        return not stack
            