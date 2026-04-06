class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # find cars that catch up to the other cars before the target
        # if the target - position / speed < car with higher position = fleet
        # count groups
        stack = []
        sort = [(p, s) for p, s in zip(position, speed)]
        sort.sort(reverse=True)
        for i in range(len(sort)):
            car = (target - sort[i][0]) / sort[i][1]
            if not stack:
                stack.append(car)
            print(stack[-1], car)
            if car > stack[-1]:
                stack.append(car)

        return len(stack)