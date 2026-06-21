class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position , speed) , reverse = True)
        arrival_times = []
        stack = []

        for i in cars:
            arrival_times.append((target - i[0])/i[1])

        for arrival in arrival_times:
            if not stack:
                stack.append(arrival)

            elif arrival > stack[-1]:
                stack.append(arrival)
            else:
                continue               
        return len(stack)