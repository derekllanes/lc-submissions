class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for tok in tokens:
            
            if tok == "+":
                cur = int(stack.pop() + stack.pop())
                stack.append(cur)
            elif tok == "-":
                B = stack.pop()
                A = stack.pop()
                cur = int(A - B)
                stack.append(cur)
            elif tok == "*":
                cur = int(stack.pop() * stack.pop())
                stack.append(cur)
            elif tok == "/":
                B = stack.pop()
                A = stack.pop()
                cur = int(A / B)
                stack.append(cur)
            else:
                stack.append(int(tok))

        return int(stack.pop())

            