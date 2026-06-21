class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position , speed) , reverse = True)
        arrival_times = []
        max_time = 0
        fleet = 0

        for i in cars:
            arrival_times.append((target - i[0])/i[1])

        for arrival in arrival_times:
            

            if arrival > max_time:
                fleet+=1
                max_time = arrival
            else:
                continue               
        return fleet