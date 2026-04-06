class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sorts = [(p, s) for p, s in zip(position, speed)]
        sorts.sort(reverse=True)
        stack = []

        for i, car in enumerate(sorts):
            if i == 0:
                stack.append((target - car[0]) / car[1])

            if ((target - car[0]) / car[1]) <= stack[-1]:
                continue
            else:
                stack.append((target - car[0]) / car[1])

        return len(stack)
