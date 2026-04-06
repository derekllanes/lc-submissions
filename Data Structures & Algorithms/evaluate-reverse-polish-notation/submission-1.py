class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []

        for op in tokens:
            if op == '+':
                b = nums.pop()
                a = nums.pop()
                nums.append(int(a+b))
            elif op == '-':
                b = nums.pop()
                a = nums.pop()
                nums.append(int(a-b))
            elif op == '*':
                b = nums.pop()
                a = nums.pop()
                nums.append(int(a*b))
            elif op == '/':
                b = nums.pop()
                a = nums.pop()
                nums.append(int(a/b))
            else:
                nums.append(int(op))

        return int(nums.pop())