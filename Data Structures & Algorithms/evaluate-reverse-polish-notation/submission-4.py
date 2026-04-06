class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for tok in tokens:
            
            if tok == "+":
                cur = int(stack.pop()) + int(stack.pop())
                stack.append(cur)
            elif tok == "-":
                B = int(stack.pop())
                A = int(stack.pop())
                cur = A - B
                stack.append(cur)
            elif tok == "*":
                cur = int(stack.pop()) * int(stack.pop())
                stack.append(cur)
            elif tok == "/":
                B = int(stack.pop())
                A = int(stack.pop())
                cur = A / B
                stack.append(cur)
            else:
                stack.append(int(tok))

        return int(stack.pop())

            